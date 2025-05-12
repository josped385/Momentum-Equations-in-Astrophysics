import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog, ttk, simpledialog
from PIL import ImageTk, Image
from scipy.optimize import curve_fit
from scipy.integrate import solve_ivp
import pandas as pd
import csv
import threading
from subprocess import call

Omega_val = phi_val = a_val = t_val = u0_val = v0_val = w0_val = x0_val = y0_val = z0_val = None
plot = plotax = plotcanvas = plotfig = None
x = y_pos = z = None

def InitializePlot():
    global plotfig, plotax, plotcanvas, plot
    # Crear el frame para la gráfica si no existe
    plot = Frame(root, bg="lightgray")
    plot.place(x=230, y=25)
    plot.grid_propagate(False)
    # Crear la figura y el eje 3D
    plotfig = Figure(figsize=(6, 5), dpi=100)
    plotax = plotfig.add_subplot(111, projection='3d')
    plotax.set_title("3D Trajectory of the Body in Space", fontsize=10)
    plotax.set_xlabel("x [m]", fontsize=10)
    plotax.set_ylabel("y [m]", fontsize=10)
    plotax.set_zlabel("z [m]", fontsize=10)
    plotax.grid(True, linestyle='--', linewidth=0.5, color="gray")
    # Crear el canvas e insertar el gráfico
    plotcanvas = FigureCanvasTkAgg(plotfig, master=plot)
    plotcanvas.get_tk_widget().pack(fill="both", expand=True)

def Calculate():
    global Omega_val, phi_val, a_val, t_val, u0_val, v0_val, w0_val, x0_val, y0_val, z0_val
    global plotax, plotcanvas, plotfig
    global x, y_pos, z

    # Parámetros
    Omega_val = float(Omega.get())
    phi_val = float(phi.get())
    a_val = float(a.get())
    t_val = float(t.get())

    # Condiciones iniciales
    u0_val = float(u0.get())
    v0_val = float(v0.get())
    w0_val = float(w0.get())
    x0_val = float(x0.get())
    y0_val = float(y0.get())
    z0_val = float(z0.get())
    initial_conditions = [u0_val, v0_val, w0_val, x0_val, y0_val, z0_val]

    # Condiciones para la simulación
    if a_val <= 0:
        messagebox.showerror('Error', 'The radius of the planet (a) must be greater than 0.')
        return
    elif t_val < 0:
        messagebox.showerror('Error', 'Simulation time (t) must be greater than 0.')
        return
    elif phi_val < -np.pi/2 or phi_val > np.pi/2:
        messagebox.showerror('Error', 'Latitude must be between -pi/2 and pi/2.')
        return

    # Definir el sistema de ecuaciones diferenciales
    def ode_system(t, y):
        # y[0]=u, y[1]=v, y[2]=w, y[3]=x, y[4]=y, y[5]=z
        du_dt = 2 * Omega_val * y[1] * np.sin(phi_val) - 2 * Omega_val * y[2] * np.cos(phi_val) - (y[0] * y[2]) / a_val + (y[0] * y[1] / a_val) * np.tan(phi_val)
        dv_dt = -2 * Omega_val * y[0] * np.sin(phi_val) - (y[0]**2 / a_val) * np.tan(phi_val)
        dw_dt = 2 * Omega_val * y[0] * np.cos(phi_val) + (y[0]**2 / a_val)
        dx_dt = y[0]  # u
        dy_dt = y[1]  # v
        dz_dt = y[2]  # w
        return [du_dt, dv_dt, dw_dt, dx_dt, dy_dt, dz_dt]

    # Dominio del tiempo para la integración
    t_span = (0, t_val)
    t_eval = np.linspace(0, t_val, 1000)

    # Resolver el sistema de ODE
    solution = solve_ivp(ode_system, t_span, initial_conditions, t_eval=t_eval, method='RK45')

    # Extraer las variables de la solución
    u = solution.y[0]
    v = solution.y[1]
    w = solution.y[2]
    x = solution.y[3]
    y_pos = solution.y[4]  # Para diferenciar del vector solución y
    z = solution.y[5]

    # Si la gráfica no ha sido inicializada, la creamos
    if plotax is None or plotcanvas is None:
        InitializePlot()

    # Agregar la nueva curva a la gráfica existente
    plotax.plot(x, y_pos, z, label=f"Curve {len(plotax.lines)+1}", linewidth=1)
    plotax.legend()
    plotcanvas.draw()
    root.update_idletasks()  # Procesa eventos pendientes
    root.update() 

def Save_fig():
    # Abre un diálogo para guardar el archivo
    filetypes = [("PNG Image", "*.png"),
                 ("JPEG Image", "*.jpg"),
                 ("SVG Image", "*.svg"),
                 ("PDF Document", "*.pdf"),
                 ("All Files", "*.*")]
    filename = filedialog.asksaveasfilename(
        title="Save Figure As",
        defaultextension=".png",
        filetypes=filetypes)
    
    if filename:
        try:
            plotfig.savefig(filename)
            messagebox.showinfo("Save Figure", f"Figure saved as:\n{filename}")
        except Exception as e:
            messagebox.showerror("Save Figure", f"Error saving figure:\n{e}")

def Save_config():
    # Crear un diccionario con los nombres y los valores actuales de cada Entry.
    data = {
        "Omega": Omega.get(),
        "phi": phi.get(),
        "a": a.get(),
        "t": t.get(),
        "u0": u0.get(),
        "v0": v0.get(),
        "w0": w0.get(),
        "x0": x0.get(),
        "y0": y0.get(),
        "z0": z0.get()
    }
    
    # Abrir un cuadro de diálogo "Guardar como..."
    filename = filedialog.asksaveasfilename(
        title="Save data in CSV",
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    if not filename:
        return  # Se canceló la selección

    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Escribir la primera fila con los nombres (cabeceras)
            headers = list(data.keys())
            writer.writerow(headers)
            # Escribir la segunda fila con los datos
            values = [data[key] for key in headers]
            writer.writerow(values)
        messagebox.showinfo("Saved", f"Data saved in:\n{filename}")
    except Exception as e:
        messagebox.showerror("Error", f"Error ocurred when saving file:\n{e}")

def Rename_curve():
    # Obtener las líneas (curvas) del eje
    lines = plotax.get_lines()
    if not lines:
        messagebox.showerror("Error", "There are no curves to rename.")
        return

    # Obtener la lista de etiquetas actuales de las curvas
    current_labels = [line.get_label() for line in lines]
    
    # Crear un mensaje que incluya las opciones disponibles
    prompt = ("Give the current name of the curve you want to rename.\n"
              "Options: " + ", ".join(current_labels))
    
    current_name = simpledialog.askstring("Select Curve", prompt)
    if current_name is None or current_name.strip() == "":
        messagebox.showerror("Error", "You must give a valid name.")
        return

    # Buscar la curva cuyo label coincide exactamente con el nombre ingresado
    selected_line = None
    for line in lines:
        if line.get_label() == current_name:
            selected_line = line
            break

    if selected_line is None:
        messagebox.showerror("Error", f"Couldn't find a curve named '{current_name}'.")
        return

    # Solicitar el nuevo nombre para la curva
    new_name = simpledialog.askstring("Rename Curve", "Give the new name for the curve:")
    if new_name is None or new_name.strip() == "":
        messagebox.showerror("Error", "You must give a valid name for the curve.")
        return

    # Actualizar la etiqueta de la curva seleccionada
    selected_line.set_label(new_name)
    
    # Actualizar la leyenda y redibujar el canvas
    plotax.legend()
    plotcanvas.draw()

def Export_Data():
    # Se asume que plotax es un objeto Axes de Matplotlib (por ejemplo, global)
    lines = plotax.get_lines()
    if not lines:
        messagebox.showerror("Error", "Couldn't find any data in the figure.")
        return

    data_dict = {}
    # Recorrer cada línea (curva)
    for idx, line in enumerate(lines):
        # Obtener la etiqueta de la curva; si no tiene etiqueta útil, se asigna un nombre por defecto.
        label = line.get_label()
        if not label or label.startswith('_'):
            label = f"Curve_{idx+1}"
        # Extraer los datos de x e y y convertirlos en un arreglo de NumPy
        x_data = np.array(line.get_xdata())
        y_data = np.array(line.get_ydata())
        # Guardar en el diccionario usando como claves el nombre de la curva + "_x" y "_y"
        data_dict[f"{label}_x"] = pd.Series(x_data)
        data_dict[f"{label}_y"] = pd.Series(y_data)

    # Crear un DataFrame con las Series; Pandas rellenará con NaN las filas faltantes
    df = pd.DataFrame(data_dict)

    # Abrir un diálogo para seleccionar dónde guardar el CSV
    filename = filedialog.asksaveasfilename(
        title="Save data as CSV",
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    if filename:
        try:
            df.to_csv(filename, index=False)
            messagebox.showinfo("Saved", f"Data saved in:\n{filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Error when saving file:\n{e}")

def Hide_curve():
    # Obtener las líneas (curvas) del eje
    lines = plotax.get_lines()
    if not lines:
        messagebox.showerror("Error", "There are no curves to hide.")
        return

    # Obtener los nombres de las curvas
    current_labels = [line.get_label() for line in lines]
    
    # Crear un mensaje que incluya las opciones disponibles
    prompt = ("Give the name of the curve you want to hide.\n"
              "Options: " + ", ".join(current_labels))
    
    curve_name = simpledialog.askstring("Select Curve", prompt)
    if curve_name is None or curve_name.strip() == "":
        messagebox.showerror("Error", "You must give a valid name.")
        return

    # Buscar la curva cuyo label coincide exactamente con el nombre ingresado
    selected_line = None
    for line in lines:
        if line.get_label() == curve_name:
            selected_line = line
            break

    if selected_line is None:
        messagebox.showerror("Error", f"Coulnd't find a curve named '{curve_name}'.")
        return

    # Ocultar la curva seleccionada
    selected_line.set_visible(False)

    # Actualizar la leyenda y redibujar el canvas
    plotax.legend()
    plotcanvas.draw()
    messagebox.showinfo("Curve has been hidden", f"The curve '{curve_name}' has been hidden.")

def Show_curve():
    # Obtener las líneas (curvas) del eje
    lines = plotax.get_lines()
    if not lines:
        messagebox.showerror("Error", "There are no curves to show.")
        return

    # Obtener los nombres de las curvas
    current_labels = [line.get_label() for line in lines]
    
    # Crear un mensaje que incluya las opciones disponibles
    prompt = ("Give the name of the curve you want to show.\n"
              "Options: " + ", ".join(current_labels))
    
    curve_name = simpledialog.askstring("Select Curve", prompt)
    if curve_name is None or curve_name.strip() == "":
        messagebox.showerror("Error", "You must give a valid name.")
        return

    # Buscar la curva cuyo label coincide exactamente con el nombre ingresado
    selected_line = None
    for line in lines:
        if line.get_label() == curve_name:
            selected_line = line
            break

    if selected_line is None:
        messagebox.showerror("Error", f"Coulnd't find a curve named '{curve_name}'.")
        return

    # Ocultar la curva seleccionada
    selected_line.set_visible(True)

    # Actualizar la leyenda y redibujar el canvas
    plotax.legend()
    plotcanvas.draw()
    messagebox.showinfo("Curve is shown", f"The curve '{curve_name}' is shown.")

def Load_curve():
    # Abrir un diálogo para seleccionar el archivo CSV
    filename = filedialog.askopenfilename(
        title="Choose CSV File",
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    if not filename:
        return  # Si se cancela la selección, no hacer nada

    try:
        # Leer los datos desde el archivo CSV
        df = pd.read_csv(filename)
    except Exception as e:
        messagebox.showerror("Error", f"Error encountered when reading CSV file:\n{e}")
        return

    # Verificar que las columnas sean pares (x, y) de acuerdo con el formato
    if len(df.columns) % 2 != 0:
        messagebox.showerror("Error", "CSV file doesn't contain a valid number of rows (must be even).")
        return

    # Recorrer las columnas del DataFrame para trazar las curvas
    for i in range(0, len(df.columns), 2):
        x_data = df.iloc[:, i]    # Columnas impares (x)
        y_data = df.iloc[:, i+1]  # Columnas pares (y)

        # Obtener el nombre de la curva desde la primera fila (nombre_x, nombre_y)
        curve_name = df.columns[i].replace('_x', '').replace('_y', '')  # Eliminar "_x" o "_y" del nombre

        try:
            # Graficar la curva
            plotax.plot(x_data, y_data, label=curve_name)
        except AttributeError:
            messagebox.showerror('Error', "In order to load data, run a measurement to create a figure. Right now, the axes don't exist, so the program doesn't know where to represent the data.")
            return

    # Actualizar la leyenda y redibujar el canvas
    plotax.legend()
    plotcanvas.draw()
    messagebox.showinfo("Data Loaded", f"Data loaded from: {filename}")

def Open_help():
    call(['python', 'HelpApp.py'])

def Open_documentation():
    call(['python', 'DocumentationApp.py'])

def Reset():
    global plotax, plotcanvas
    if plotax is not None:
        # Limpiar el eje
        plotax.cla()
        # Reconfigurar el gráfico
        plotax.set_title("3D Trajectory of the Body in Space", fontsize=10)
        plotax.set_xlabel("x [m]", fontsize=10)
        plotax.set_ylabel("y [m]", fontsize=10)
        plotax.set_zlabel("z [m]", fontsize=10)
        plotax.grid(True, linestyle='--', linewidth=0.5, color="gray")
        # Actualizar el canvas
        plotcanvas.draw()

def Change(event):
    selected_planet = CommonPlanetsDropDown_value.get()  # Obtener el planeta seleccionado
    params = planet_params[selected_planet]  # Obtener los parámetros del planeta seleccionado
    
    # Actualizar los valores de los Entry
    a.delete(0, tk.END)  # Limpiar el campo de entrada
    Omega.delete(0, tk.END)
    
    a.insert(0, str(params['a']))  # Insertar el valor del radio
    Omega.insert(0, str(params['Omega']))  # Insertar el valor de Omega

def AngleCalculator():
    call(['python', 'AngleCalculator.py'])

root = tk.Tk()
root.title("Momentum Equations in Astrophysics Application")
root.iconbitmap('US-marca-principal.ico')
root.geometry("914x668")
root.resizable(False, False)

# Crear un menú bar
menubar = Menu(root)

# Crear el menú "File" y sus opciones
file_menu = Menu(menubar, tearoff=0)
# Crear el submenú para 'Save Figure'
file_menu.add_command(label="Save Figure", command=Save_fig)
file_menu.add_command(label="Save Config", command=Save_config)
file_menu.add_command(label="Rename Curve", command=Rename_curve)
file_menu.add_command(label="Export Data", command=Export_Data)
file_menu.add_command(label="Hide Curve", command=Hide_curve)
file_menu.add_command(label="Show Curve", command=Show_curve)
file_menu.add_command(label="Load Curve", command=Load_curve)
file_menu.add_command(label="Angle Calculator", command=AngleCalculator)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Crear el menú "Help" y sus opciones
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="Help", command=Open_help)
help_menu.add_command(label="Documentation", command=Open_documentation)

# Agregar los menús al menú bar
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Help", menu=help_menu)

# Configurar el menú de la ventana principal
root.config(menu=menubar)

InitializePlot()

Calculate = Button(root, text="Calculate", command=Calculate)
Calculate.place(x=80, y=668-614)

# Create the Planet Angular Velocity Panel
PlanetAngularVelocity = LabelFrame(root, text="Planet's Angular Velocity (rad/s)", width=180, height=75, padx=10, pady=10)
PlanetAngularVelocity.place(x=27, y=668-550)
PlanetAngularVelocity.grid_propagate(False)

# Create label for Omega
Omega_label = Label(PlanetAngularVelocity, text="Omega", padx=10, pady=5)
Omega_label.grid(row=0, column=0, sticky="e")

# Create the Omega Edit Field
Omegadefault = IntVar()
Omegadefault.set(0)
Omega = Entry(PlanetAngularVelocity, width=10, textvariable=Omegadefault)
Omega.grid(row=0, column=1, sticky="w")

# Create the Latitude Panel
Latitude = LabelFrame(root, text="Latitude (rad)", width=180, height=75, padx=10, pady=10)
Latitude.place(x=27, y=668-475)
Latitude.grid_propagate(False)

# Create label for phi
phi_label = Label(Latitude, text="phi", padx=10, pady=5)
phi_label.grid(row=0, column=0, sticky="e")

# Create the phi Edit Field
phidefault = IntVar()
phidefault.set(0)
phi = Entry(Latitude, width=10, textvariable=phidefault)
phi.grid(row=0, column=1, sticky="w")

# Create the Planet Radius Panel
PlanetRadius = LabelFrame(root, text="Planet Radius (m)", width=180, height=75, padx=10, pady=10)
PlanetRadius.place(x=27, y=668-400)
PlanetRadius.grid_propagate(False)

# Create label for a
a_label = Label(PlanetRadius, text="a", padx=10, pady=5)
a_label.grid(row=0, column=0, sticky="e")

# Create the a Edit Field
adefault = IntVar()
adefault.set(0)
a = Entry(PlanetRadius, width=10, textvariable=adefault)
a.grid(row=0, column=1, sticky="w")

# Create the Simulation Time Panel
SimulationTime = LabelFrame(root, text="Simulation Time (s)", width=180, height=75, padx=10, pady=10)
SimulationTime.place(x=27, y=668-325)
SimulationTime.grid_propagate(False)

# Create label for t
t_label = Label(SimulationTime, text="t", padx=10, pady=5)
t_label.grid(row=0, column=0, sticky="e")

# Create the t Edit Field
tdefault = IntVar()
tdefault.set(0)
t = Entry(SimulationTime, width=10, textvariable=tdefault)
t.grid(row=0, column=1, sticky="w")

# Create the Initial Conditions Panel
InitialConditions = LabelFrame(root, text="Initial Conditions (in IS Units)", width=180, height=210, padx=10, pady=10)
InitialConditions.place(x=27, y=668-250)
InitialConditions.grid_propagate(False)

# Create label for u0
u0_label = Label(InitialConditions, text="u0", padx=10, pady=5)
u0_label.grid(row=0, column=0, sticky="e")

# Create the u0 Edit Field
u0default = IntVar()
u0default.set(0)
u0 = Entry(InitialConditions, width=10, textvariable=u0default)
u0.grid(row=0, column=1, sticky="w")

# Create label for v0
v0_label = Label(InitialConditions, text="v0", padx=10, pady=5)
v0_label.grid(row=1, column=0, sticky="e")

# Create the v0 Edit Field
v0default = IntVar()
v0default.set(0)
v0 = Entry(InitialConditions, width=10, textvariable=v0default)
v0.grid(row=1, column=1, sticky="w")

# Create label for w0
w0_label = Label(InitialConditions, text="w0", padx=10, pady=5)
w0_label.grid(row=2, column=0, sticky="e")

# Create the w0 Edit Field
w0default = IntVar()
w0default.set(0)
w0 = Entry(InitialConditions, width=10, textvariable=w0default)
w0.grid(row=2, column=1, sticky="w")

# Create label for x0
x0_label = Label(InitialConditions, text="x0", padx=10, pady=5)
x0_label.grid(row=3, column=0, sticky="e")

# Create the x0 Edit Field
x0default = IntVar()
x0default.set(0)
x0 = Entry(InitialConditions, width=10, textvariable=x0default)
x0.grid(row=3, column=1, sticky="w")

# Create label for y0
y0_label = Label(InitialConditions, text="y0", padx=10, pady=5)
y0_label.grid(row=4, column=0, sticky="e")

# Create the y0 Edit Field
y0default = IntVar()
y0default.set(0)
y0 = Entry(InitialConditions, width=10, textvariable=y0default)
y0.grid(row=4, column=1, sticky="w")

# Create label for z0
z0_label = Label(InitialConditions, text="z0", padx=10, pady=5)
z0_label.grid(row=5, column=0, sticky="e")

# Create the z0 Edit Field
z0default = IntVar()
z0default.set(0)
z0 = Entry(InitialConditions, width=10, textvariable=z0default)
z0.grid(row=5, column=1, sticky="w")

# Cargar y redimensionar la imagen de US
US = Image.open("US-marca-principal.png")  # Cambia por la ruta de tu imagen
US_resized = US.resize((100, 90))  # Cambia el tamaño (ancho, alto)
US_photo = ImageTk.PhotoImage(US_resized)
US_label = Label(root, image=US_photo)
US_label.place(x=784, y=668-135)  # Cambia la posición (x, y)

Reset = Button(root, text="Reset Figure", command=Reset)
Reset.place(x=626, y=668-90)

# Create the Common Planets panel
CommonPlanets = LabelFrame(root, text="Common Planets", width=180, height=75, padx=10, pady=10)
CommonPlanets.place(x=360, y=668-115)
CommonPlanets.grid_propagate(False)

# Create the Common Planets DropDown
CommonPlanetsDropDown_options = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
CommonPlanetsDropDown_value = StringVar(value=CommonPlanetsDropDown_options[0])
CommonPlanetsDropDown = OptionMenu(CommonPlanets, CommonPlanetsDropDown_value, *CommonPlanetsDropDown_options)
CommonPlanetsDropDown.grid(row=0, column=0, padx=10, pady=1)
# Asociar la función Change con el evento de selección del planeta
CommonPlanetsDropDown.bind("<Configure>", Change)

# Definir los parámetros de cada planeta
planet_params = {
    'Mercury': {'a': 2439.7e3, 'Omega': 4.092e-6},
    'Venus': {'a': 6051.8e3, 'Omega': 1.175e-7},
    'Earth': {'a': 6371e3, 'Omega': 7.2921e-5},
    'Mars': {'a': 3389.5e3, 'Omega': 7.088e-5},
    'Jupiter': {'a': 69911e3, 'Omega': 1.7585e-4},
    'Saturn': {'a': 58232e3, 'Omega': 1.664e-4},
    'Uranus': {'a': 25362e3, 'Omega': 1.562e-5},
    'Neptune': {'a': 24622e3, 'Omega': 1.663e-5},
}

root.mainloop()
