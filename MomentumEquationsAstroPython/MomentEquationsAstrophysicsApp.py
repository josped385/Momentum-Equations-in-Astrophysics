import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog, simpledialog
from PIL import ImageTk, Image
from scipy.integrate import solve_ivp
import pandas as pd
import csv

class HelpWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Help")
        self.iconbitmap("US-marca-principal.ico")
        self.geometry("900x670")
        self.resizable(False, False)
        self.help_frame = tk.Frame(self)
        self.help_frame.pack()

        # Build UI
        self._create_controls()

        # Clean reference in master so the window can be opened again
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        """
        Cleans the reference in master so it can be opened again
        :return:
        """
        if hasattr(self.master, "help_win"):
            try:
                self.master.help_win = None
            except Exception as e:
                print("Error en:", e)
                raise
        self.destroy()

    def _create_controls(self):
        """
        Creates the control widgets
        :return:
        """

        # Label that works as a title for the window
        tk.Label(self.help_frame, text="HELP FOR MOMENTUM EQUATIONS IN ASTROPHYSICS").pack(padx=10, pady=10)

        # Load and redraw the image of the momentum equations
        momentum_photo = Image.open("momentum_equations.png")
        momentum_photo_resized = momentum_photo.resize((450, 221))
        self.momentum_photo_photo = ImageTk.PhotoImage(momentum_photo_resized)
        self.momentum_photo_label = Label(self.help_frame, image=self.momentum_photo_photo)
        self.momentum_photo_label.pack(padx=10, pady=10)

        # Create a scrollbar for functionalities
        scrollbar = tk.Scrollbar(self.help_frame)
        scrollbar.pack(side="right", fill="y")

        # Create the text in functionalities
        func_text = Text(self.help_frame, height=50, yscrollcommand=scrollbar.set)
        func_text.pack(padx=10, pady=10, fill='both', expand=True)

        # Open and read file
        func_open = open('help_functionalities.txt', 'r')
        func_read = func_open.read()
        func_text.insert(END, func_read)
        func_open.close()
        scrollbar.config(command=func_text.yview)

class DocumentationWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Documentation")
        self.iconbitmap("US-marca-principal.ico")
        self.geometry("640x480")
        self.resizable(False, False)
        self.doc_frame = tk.Frame(self)
        self.doc_frame.pack()

        # Build UI
        self._create_controls()

        # Clean reference in master so the window can be opened again
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        """
        Cleans the reference in master so it can be opened again
        :return:
        """
        if hasattr(self.master, "doc_win"):
            try:
                self.master.doc_win = None
            except Exception as e:
                print("Error en:", e)
                raise
        self.destroy()

    def _create_controls(self):
        """
        Creates the control widgets
        :return:
        """

        # Label that works as a title for the window
        tk.Label(self.doc_frame, text="DOCUMENTATION FOR MOMENTUM EQUATIONS IN ASTROPHYSICS").pack(padx=10, pady=10)

        # Create a scrollbar for functionalities
        scrollbar = tk.Scrollbar(self.doc_frame)
        scrollbar.pack(side="right", fill="y")

        # Create the text in functionalities
        func_text = Text(self.doc_frame, height=50, yscrollcommand=scrollbar.set)
        func_text.pack(padx=10, pady=10, fill='both', expand=True)

        # Open and read file
        func_open = open('documentation.txt', 'r')
        func_read = func_open.read()
        func_text.insert(END, func_read)
        func_open.close()
        scrollbar.config(command=func_text.yview)

class AboutWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Documentation")
        self.iconbitmap("US-marca-principal.ico")
        self.geometry("640x480")
        self.resizable(False, False)
        self.about_frame = tk.Frame(self)
        self.about_frame.pack()

        # Build UI
        self._create_controls()

        # Clean reference in master so the window can be opened again
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        """
        Cleans the reference in master so it can be opened again
        :return:
        """
        if hasattr(self.master, "about_win"):
            try:
                self.master.about_win = None
            except Exception as e:
                print("Error en:", e)
                raise
        self.destroy()

    def _create_controls(self):
        """
        Creates the control widgets
        :return:
        """

        # Label that works as a title for the window
        tk.Label(self.about_frame, text="ABOUT THIS APP").pack(padx=10, pady=10)

        # Create a scrollbar for functionalities
        scrollbar = tk.Scrollbar(self.about_frame)
        scrollbar.pack(side="right", fill="y")

        # Create the text in functionalities
        func_text = Text(self.about_frame, height=50, yscrollcommand=scrollbar.set)
        func_text.pack(padx=10, pady=10, fill='both', expand=True)

        # Open and read file
        func_open = open('about.txt', 'r')
        func_read = func_open.read()
        func_text.insert(END, func_read)
        func_open.close()
        scrollbar.config(command=func_text.yview)

class AngleCalculator(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Angle Calculator")
        self.iconbitmap("US-marca-principal.ico")
        self.geometry("350x240")
        self.resizable(False, False)
        self.angle_frame = tk.Frame(self)
        self.angle_frame.pack()

        # Build UI
        self._create_controls()

        # Clean reference in master so the window can be opened again
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        """
        Cleans the reference in master so it can be opened again
        :return:
        """
        if hasattr(self.master, "angle_win"):
            try:
                self.master.angle_win = None
            except Exception as e:
                print("Error en:", e)
                raise
        self.destroy()

    def _create_controls(self):
        """
        Creates the control widgets
        :return:
        """
        # Button for Convert
        tk.Button(self.angle_frame, text='Convert', command=self.ang_converter).grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # Label for d-r calculator
        tk.Label(self.angle_frame, text='Degrees to radians calculator').grid(row=1, column=0, columnspan=5, padx=10, pady=10)

        # Label for 'Degrees'
        tk.Label(self.angle_frame, text='Degrees', padx=10, pady=5).grid(row=2, column=0, sticky="e", pady=10)

        # Entry for 'Degrees'
        d1_default = tk.IntVar(value=0)
        self.d1 = tk.Entry(self.angle_frame, width=10, textvariable=d1_default)
        self.d1.grid(row=2, column=1, sticky="w", padx=5, pady=10)

        # Label with arrow
        tk.Label(self.angle_frame, text='->').grid(row=2, column=2, padx=10, pady=10)

        # Label for 'Radians'
        tk.Label(self.angle_frame, text='Radians', padx=10, pady=5).grid(row=2, column=3, sticky="e", pady=10)

        # Entry for 'Radians'
        r1_default = tk.IntVar(value=0)
        self.r1 = tk.Entry(self.angle_frame, width=10, textvariable=r1_default)
        self.r1.grid(row=2, column=4, sticky="w", padx=5, pady=10)

        # Label for r-d calculator
        tk.Label(self.angle_frame, text='Radians to degrees calculator').grid(row=3, column=0, columnspan=5, padx=10, pady=10)

        # Label for 'Radians'
        tk.Label(self.angle_frame, text='Radians', padx=10, pady=5).grid(row=4, column=0, sticky="e", pady=10)

        # Entry for 'Radians'
        r2_default = tk.IntVar(value=0)
        self.r2 = tk.Entry(self.angle_frame, width=10, textvariable=r2_default)
        self.r2.grid(row=4, column=1, sticky="w", padx=5, pady=10)

        # Label for arrow
        tk.Label(self.angle_frame, text='->').grid(row=4, column=2, padx=10, pady=10)

        # Label for 'Degrees'
        tk.Label(self.angle_frame, text='Degrees', padx=10, pady=5).grid(row=4, column=3, sticky="e", pady=10)

        # Entry for 'Degrees'
        d2_default = tk.IntVar(value=0)
        self.d2 = tk.Entry(self.angle_frame, width=10, textvariable=d2_default)
        self.d2.grid(row=4, column=4, sticky="w", padx=5, pady=10)

    def ang_converter(self):
        """
        Converts degrees to radians and vice versa
        :return:
        """
        deg1 = float(self.d1.get())
        rad2 = float(self.r2.get())

        rad1 = deg1 / 180 * np.pi
        deg2 = rad2 * 180 / np.pi

        # Clean the rad1 and deg2 Entry
        self.r1.delete(0, tk.END)
        self.d2.delete(0, tk.END)

        # Assign results to the Entry
        self.r1.insert(0, f'{rad1: .7g}')
        self.d2.insert(0, f'{deg2: .7g}')

class MomentumEquationsAstrophysicsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Momentum Equations in Astrophysics")
        self.iconbitmap("US-marca-principal.ico")
        self.geometry("900x700")
        self.resizable(False, False)

        # Build UI
        self._create_menu()
        self._create_controls()
        self._change(None)
        self.angle_win = None
        self.help_win = None
        self.doc_win = None
        self.about_win = None
        self._load_us_logo()

        # Plot data
        self.curves = []
        self.curve_count = 0

    def _create_menu(self):
        """
        Creates the menu widgets
        :return:
        """
        menubar = tk.Menu(self)
        files_menu = tk.Menu(menubar, tearoff=False)
        files_menu.add_command(label='Save Figure', command=self.save_figure)
        files_menu.add_command(label='Save Config', command=self.save_config)
        files_menu.add_command(label='Rename Curve', command=self.rename)
        files_menu.add_command(label='Export Data', command=self.export_data)
        files_menu.add_command(label='Hide Curve', command=self.hide_curve)
        files_menu.add_command(label='Show Curve', command=self.show_curve)
        files_menu.add_command(label='Load Data', command=self.load_data)
        files_menu.add_command(label='Angle Calculator', command=self.open_angle_calculator)
        menubar.add_cascade(label='File', menu=files_menu)

        helps_menu = tk.Menu(menubar, tearoff=False)
        helps_menu.add_command(label='Help', command=self.open_help_window)
        helps_menu.add_command(label='Documentation', command=self.open_doc_window)
        helps_menu.add_command(label='About', command=self.open_about_window)
        menubar.add_cascade(label="Help", menu=helps_menu)

        self.config(menu=menubar)

    def _create_controls(self):
        """
        Creates the control widgets
        :return:
        """
        frame = tk.Frame(self)
        frame.pack(fill="both", expand=True)

        # Button for 'Calculate'
        tk.Button(frame, text='Calculate', command=self.calculate).place(x=80, y=54)

        # Panel for pav (pav stands for Planet's Angular Velocity)
        pav = tk.LabelFrame(frame, text="Planet's Angular Velocity (rad/s)", width=180, height=75, padx=10, pady=10)
        pav.place(x=27, y=118)
        pav.grid_propagate(True)

        # Label for omega
        tk.Label(pav, text='Omega').grid(row=0, column=0, sticky="e", padx=10, pady=5)

        # Entry for omega
        omega_default = tk.IntVar(value=0)
        self.omega = tk.Entry(pav, width=10, textvariable=omega_default)
        self.omega.grid(row=0, column=1, sticky="w")

        # Panel for latitude
        latitude = tk.LabelFrame(frame, text="Latitude (rad)", width=180, height=75, padx=10, pady=10)
        latitude.place(x=27, y=193)
        latitude.grid_propagate(False)

        # Label for phi
        tk.Label(latitude, text='phi', padx=10, pady=5).grid(row=0, column=0, sticky="e")

        # Entry for phi
        phi_default = tk.IntVar(value=0)
        self.phi = tk.Entry(latitude, width=10, textvariable=phi_default)
        self.phi.grid(row=0, column=1, sticky="w")

        # Panel for pr (pr stands for Planet Radius)
        pr = LabelFrame(frame, text="Planet Radius (m)", width=180, height=75, padx=10, pady=10)
        pr.place(x=27, y=268)
        pr.grid_propagate(False)

        # Label for a
        tk.Label(pr, text="a", padx=10, pady=5).grid(row=0, column=0, sticky="e")

        # Entry for a
        a_default = tk.IntVar(value=0)
        self.a = tk.Entry(pr, width=10, textvariable=a_default)
        self.a.grid(row=0, column=1, sticky="w")

        # Panel for st (st stands for Simulation Time)
        st = tk.LabelFrame(frame, text='Simulation Time (s)', width=180, height=75, padx=10, pady=10)
        st.place(x=27, y=343)
        st.grid_propagate(False)

        # Label for t
        tk.Label(st, text='t', padx=10, pady=5).grid(row=0, column=0, sticky="e")

        # Entry for t
        t_default = tk.IntVar(value=0)
        self.t = tk.Entry(st, width=10, textvariable=t_default)
        self.t.grid(row=0, column=1, sticky="w")

        # Panel for ic (ic stands for Initial Conditions)
        ic = tk.LabelFrame(frame, text="Initial Conditions (in IS Units)", width=180, height=210, padx=10, pady=10)
        ic.place(x=27, y=418)
        ic.grid_propagate(True)

        # Label for u0
        tk.Label(ic, text='u0', padx=10, pady=5).grid(row=0, column=0, sticky="e")

        # Entry for u0
        u0_default = tk.IntVar(value=0)
        self.u0 = tk.Entry(ic, width=10, textvariable=u0_default)
        self.u0.grid(row=0, column=1, sticky="w")

        # Label for v0
        tk.Label(ic, text='v0', padx=10, pady=5).grid(row=1, column=0, sticky="e")

        # Entry for v0
        v0_default = tk.IntVar(value=0)
        self.v0 = tk.Entry(ic, width=10, textvariable=v0_default)
        self.v0.grid(row=1, column=1, sticky="w")

        # Label for w0
        tk.Label(ic, text='w0', padx=10, pady=5).grid(row=2, column=0, sticky="e")

        # Entry for w0
        w0_default = tk.IntVar(value=0)
        self.w0 = tk.Entry(ic, width=10, textvariable=w0_default)
        self.w0.grid(row=2, column=1, sticky="w")

        # Label for x0
        tk.Label(ic, text='x0', padx=10, pady=5).grid(row=3, column=0, sticky="e")

        # Entry for x0
        x0_default = tk.IntVar(value=0)
        self.x0 = tk.Entry(ic, width=10, textvariable=x0_default)
        self.x0.grid(row=3, column=1, sticky="w")

        # Label for y0
        tk.Label(ic, text='y0', padx=10, pady=5).grid(row=4, column=0, sticky="e")

        # Entry for y0
        y0_default = tk.IntVar(value=0)
        self.y0 = tk.Entry(ic, width=10, textvariable=y0_default)
        self.y0.grid(row=4, column=1, sticky="w")

        # Label for z0
        tk.Label(ic, text='z0', padx=10, pady=5).grid(row=5, column=0, sticky="e")

        # Entry for z0
        z0_default = tk.IntVar(value=0)
        self.z0 = tk.Entry(ic, width=10, textvariable=z0_default)
        self.z0.grid(row=5, column=1, sticky="w")

        # Button for Reset
        tk.Button(frame, text='Reset', command=self.reset).place(x=626, y=590)

        # Panel for cp (cp stands for Common Planets)
        cp_frame = tk.LabelFrame(frame, text="Common Planets", width=180, height=75, padx=10, pady=10)
        cp_frame.place(x=340, y=560)
        cp_frame.grid_propagate(False)

        # Drop Down for Common Planets
        cp_options = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
        self.cp_default = tk.StringVar(value=cp_options[0])
        cp_menu = tk.OptionMenu(cp_frame, self.cp_default, *cp_options)
        cp_menu.grid(row=0, column=0, padx=10, pady=1)
        cp_menu.bind('<Configure>', self._change)

        # Define the parameters of each planet
        self.planet_params = {
            'Mercury': {'a': 2439.7e3, 'Omega': 4.092e-6},
            'Venus': {'a': 6051.8e3, 'Omega': 1.175e-7},
            'Earth': {'a': 6371e3, 'Omega': 7.2921e-5},
            'Mars': {'a': 3389.5e3, 'Omega': 7.088e-5},
            'Jupiter': {'a': 69911e3, 'Omega': 1.7585e-4},
            'Saturn': {'a': 58232e3, 'Omega': 1.664e-4},
            'Uranus': {'a': 25362e3, 'Omega': 1.562e-5},
            'Neptune': {'a': 24622e3, 'Omega': 1.663e-5},
        }

        # Create matplotlib figure and canvas
        self.fig = Figure(figsize=(6, 5), dpi=100)
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_title("3D Trajectory of the Body in Space", fontsize=10)
        self.ax.set_xlabel("x [m]", fontsize=10)
        self.ax.set_ylabel("y [m]", fontsize=10)
        self.ax.set_zlabel("z [m]", fontsize=10)
        self.ax.grid(True, linestyle='--', linewidth=0.5, color="gray")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().place(x=240, y=54, width=640, height=480)

    def _load_us_logo(self):
        """
        Loads University of Seville logo (decorative item)
        :return:
        """
        us = Image.open("US-marca-principal.png")
        us_resized = us.resize((100, 90))
        self.us_photo = ImageTk.PhotoImage(us_resized)
        self.us_label = tk.Label(self, image=self.us_photo)
        self.us_label.place(x=764, y=540)

    def _change(self, event):
        """
        Changes the values of 'a' and 'omega' when the Common Planets Drop Down is changed
        :param event:
        :return:
        """
        selected_planet = self.cp_default.get()  # Obtain the selected planet
        params = self.planet_params.get(selected_planet, None)
        if not params:
            return

        # Renew the Entry values
        try:
            self.a.delete(0, tk.END)  # Clean the Entry field
            self.omega.delete(0, tk.END)

            self.a.insert(0, str(params['a']))  # Insert the value of the radius
            self.omega.insert(0, str(params['Omega']))  # Insert the value of omega
        except Exception as e:
            print("Error en:", e)
            raise

    def open_angle_calculator(self, modal=False):
        """
        If it doesn't exist, we create the window, if it exists, we bring it forward
        :param modal:
        :return:
        """
        if self.angle_win is None or not tk.Toplevel.winfo_exists(self.angle_win):
            self.angle_win = AngleCalculator(self)
            if modal:
                # We make it modal (optional)
                self.angle_win.transient(self)   # Window on top of the main one
                self.angle_win.grab_set()        # Blocks interactions with the main one
                self.wait_window(self.angle_win) # Waits until it is closed
        else:
            # If it already exists, we bring it forward and highlight it
            try:
                self.angle_win.lift()
                self.angle_win.focus_force()
            except Exception as e:
                print("Error en:", e)
                raise

    def open_help_window(self, modal=False):
        """
        If it doesn't exist, we create the window, if it exists, we bring it forward
        :param modal:
        :return:
        """
        if self.help_win is None or not tk.Toplevel.winfo_exists(self.help_win):
            self.help_win = HelpWindow(self)
            if modal:
                # We make it modal (optional)
                self.help_win.transient(self)   # Window on top of the main one
                self.help_win.grab_set()        # Blocks interactions with the main one
                self.wait_window(self.help_win) # Waits until it is closed
        else:
            # If it already exists, we bring it forward and highlight it
            try:
                self.help_win.lift()
                self.help_win.focus_force()
            except Exception as e:
                print("Error en:", e)
                raise

    def open_doc_window(self, modal=False):
        """
        If it doesn't exist, we create the window, if it exists, we bring it forward
        :param modal:
        :return:
        """
        if self.doc_win is None or not tk.Toplevel.winfo_exists(self.doc_win):
            self.doc_win = DocumentationWindow(self)
            if modal:
                # We make it modal (optional)
                self.doc_win.transient(self)   # Window on top of the main one
                self.doc_win.grab_set()        # Blocks interactions with the main one
                self.wait_window(self.doc_win) # Waits until it is closed
        else:
            # If it already exists, we bring it forward and highlight it
            try:
                self.doc_win.lift()
                self.doc_win.focus_force()
            except Exception as e:
                print("Error en:", e)
                raise

    def open_about_window(self, modal=False):
        """
        If it doesn't exist, we create the window, if it exists, we bring it forward
        :param modal:
        :return:
        """
        if self.about_win is None or not tk.Toplevel.winfo_exists(self.about_win):
            self.about_win = AboutWindow(self)
            if modal:
                # We make it modal (optional)
                self.about_win.transient(self)   # Window on top of the main one
                self.about_win.grab_set()        # Blocks interactions with the main one
                self.wait_window(self.about_win) # Waits until it is closed
        else:
            # If it already exists, we bring it forward and highlight it
            try:
                self.about_win.lift()
                self.about_win.focus_force()
            except Exception as e:
                print("Error en:", e)
                raise

    def _add_curve(self, xs, ys, zs, label=None):
        """
        Adds the loaded curve to the axes.
        :param xs:
        :param ys:
        :param label:
        :return:
        """
        lbl = label or f"Curve {self.curve_count+1}"
        line = self.ax.plot(xs, ys, zs, label=lbl)
        self.curve_count += 1
        self.curves.append({'x': xs.copy(), 'y': ys.copy(), 'line': line, 'label': lbl, 'visible': True})
        self.ax.legend()
        self.canvas.draw()

    # File menu functions
    def save_figure(self):
        """
        Saves the figure to disk.
        :return:
        """
        types = [('PNG', '*.png'), ('JPG', '*.jpg'), ('PDF', '*.pdf'), ('SVG', '*.svg'), ('JPEG', '*.jpeg')]
        filename = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes=types)
        if filename:
            self.fig.savefig(filename)

    def load_data(self):
        """
        Loads the data from disk.
        :return:
        """
        filename = filedialog.askopenfilename(filetypes=[('CSV', '*.csv')])
        if not filename:
            return
        with open(filename) as f:
            reader = csv.reader(f)
            next(reader, None)
            xs, ys = zip(*[(float(r[0]), float(r[1])) for r in reader])
        self._add_curve(list(xs), list(ys), list(zs))

    def rename(self):
        """
        Renames the curves to a desired name
        :return:
        """

        # Get the current lines from the figure
        lines = self.ax.get_lines()
        if not lines:
            messagebox.showerror("Error", "No lines to rename")
            return

        # Get the current names of the curves
        current_labels = [line.get_label() for line in lines]

        # Create a prompt with the curves available
        prompt = ("Give the current name of the curve you want to rename.\n"
              "Options: " + ", ".join(current_labels))

        current_name = simpledialog.askstring("Select Curve", prompt)
        if current_name is None or current_name.strip() == "":
            messagebox.showerror("Error", "You must give a valid name.")
            return

        # Search for the curve whose label match exactly with the name provided
        selected_line = None
        for line in lines:
            if line.get_label() == current_name:
                selected_line = line
                break

        if selected_line is None:
            messagebox.showerror("Error", f"Couldn't find a curve named '{current_name}'.")
            return

        # Ask for the new name for the curve
        new_name = simpledialog.askstring("Rename Curve", "Give the new name for the curve:")
        if new_name is None or new_name.strip() == "":
            messagebox.showerror("Error", "You must give a valid name for the curve.")
            return

        # Refresh the label of the selected curve
        selected_line.set_label(new_name)

        # Refresh the legend and redraw the canvas
        self.ax.legend()
        self.canvas.draw()

    def save_config(self):
        """
        Saves the parameters stored in the Entry
        :return:
        """

        # Create a dictionary with the names and values of the current parameters
        data = {
            "Omega": self.omega.get(),
            "phi": self.phi.get(),
            "a": self.a.get(),
            "t": self.t.get(),
            "u0": self.u0.get(),
            "v0": self.v0.get(),
            "w0": self.w0.get(),
            "x0": self.x0.get(),
            "y0": self.y0.get(),
            "z0": self.z0.get()
        }

        # Open the prompt to save the parameters
        filename = filedialog.asksaveasfilename(
            title="Save data in CSV",
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
        )
        if not filename:
            return  # Selection was cancelled

        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                # Write the first row with the names
                headers = list(data.keys())
                writer.writerow(headers)
                # Write the second row with the data
                values = [data[key] for key in headers]
                writer.writerow(values)
            messagebox.showinfo("Saved", f"Data saved in:\n{filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred when saving file:\n{e}")

    def export_data(self):
        """
        Exports the data of the curves drawn in the figure
        :return:
        """

        # Let's take the curves represented in the figure
        lines = self.ax.get_lines()
        if not lines:
            messagebox.showerror("Error", "Couldn't find any data in the figure.")
            return

        data_dict = {}
        # Go over each curve
        for idx, line in enumerate(lines):
            # Obtain the label of the curve; if it doesn't have a label, we provide one
            label = line.get_label()
            if not label or label.startswith('_'):
                label = f"Curve_{idx + 1}"
            # Extract the data and turn it into an array using NumPy
            x_data = np.array(line.get_xdata())
            y_data = np.array(line.get_ydata())
            # Save it in a dict using as keys the name of the curve + "_x" and "_y"
            data_dict[f"{label}_x"] = pd.Series(x_data)
            data_dict[f"{label}_y"] = pd.Series(y_data)

        # Create a dataframe with the Series; Pandas will fill with NaN the rest of the rows
        df = pd.DataFrame(data_dict)

        # Open a dialog to choose where to save the csv file
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

    def hide_curve(self):
        """
        Hides the chosen curve (but doesn't delete it)
        :return:
        """

        # Get the curves from the axes
        lines = self.ax.get_lines()
        if not lines:
            messagebox.showerror("Error", "There are no curves to hide.")
            return

        # Obtain the name of the curves
        current_labels = [line.get_label() for line in lines]

        # Create a prompt with the available curves to choose
        prompt = ("Give the name of the curve you want to hide.\n"
                  "Options: " + ", ".join(current_labels))

        curve_name = simpledialog.askstring("Select Curve", prompt)
        if curve_name is None or curve_name.strip() == "":
            messagebox.showerror("Error", "You must give a valid name.")
            return

        # Search for the curve whose name coincides with the name introduced in the prompt
        selected_line = None
        for line in lines:
            if line.get_label() == curve_name:
                selected_line = line
                break

        if selected_line is None:
            messagebox.showerror("Error", f"Couldn't find a curve named '{curve_name}'.")
            return

        # Hide the selected curve
        selected_line.set_visible(False)

        # Refresh the legend and redraw the canvas
        self.ax.legend()
        self.canvas.draw()
        messagebox.showinfo("Curve has been hidden", f"The curve '{curve_name}' has been hidden.")

    def show_curve(self):
        """
        If the curve was hidden, this helps to turn the visibility on
        :return:
        """

        # Get the curves from the axis
        lines = self.ax.get_lines()
        if not lines:
            messagebox.showerror("Error", "There are no curves to show.")
            return

        # Get the names of the curves
        current_labels = [line.get_label() for line in lines]

        # Create a message with the available options
        prompt = ("Give the name of the curve you want to show.\n"
                  "Options: " + ", ".join(current_labels))

        curve_name = simpledialog.askstring("Select Curve", prompt)
        if curve_name is None or curve_name.strip() == "":
            messagebox.showerror("Error", "You must give a valid name.")
            return

        # Search for the curve whose name coincides with the name provided
        selected_line = None
        for line in lines:
            if line.get_label() == curve_name:
                selected_line = line
                break

        if selected_line is None:
            messagebox.showerror("Error", f"Couldn't find a curve named '{curve_name}'.")
            return

        # Show the selected curve
        selected_line.set_visible(True)

        # Refresh the axis and redraw the canvas
        self.ax.legend()
        self.canvas.draw()
        messagebox.showinfo("Curve is shown", f"The curve '{curve_name}' is shown.")

    def calculate(self):
        """
        Calculate the curve described by the planet using momentum equations given the initial conditions specified
        :return:
        """

        # Let's turn parameters into float
        try:
            a = float(self.a.get())
            omega = float(self.omega.get())
            phi = float(self.phi.get())
            t = float(self.t.get())
        except Exception:
            messagebox.showerror('Error', 'Please ensure a, omega, phi and t are numeric values.')
            return

        # Let's turn initial conditions into float, and then store them in a list
        try:
            u0 = float(self.u0.get())
            v0 = float(self.v0.get())
            w0 = float(self.w0.get())
            x0 = float(self.x0.get())
            y0 = float(self.y0.get())
            z0 = float(self.z0.get())
        except Exception:
            messagebox.showerror('Error', 'Please ensure initial conditions are numeric.')
            return

        initial_conditions = [u0, v0, w0, x0, y0, z0]

        # Check that fields make sense
        if a <= 0:
            messagebox.showerror('Error', 'The radius of the planet (a) must be greater than 0 meters.')
            return
        elif t <= 0:
            messagebox.showerror('Error', 'Simulation time (t) must be greater than 0 seconds.')
            return
        elif phi < -np.pi / 2 or phi > np.pi / 2:
            messagebox.showerror('Error', 'Latitude must be between -pi/2 and pi/2 radians.')
            return

        def ode_system(t_var, y):
            # y[0]=u, y[1]=v, y[2]=w, y[3]=x, y[4]=y, y[5]=z
            du_dt = 2 * omega * y[1] * np.sin(phi) - 2 * omega * y[2] * np.cos(phi) - (
                        y[0] * y[2]) / a + (y[0] * y[1] / a) * np.tan(phi)
            dv_dt = -2 * omega * y[0] * np.sin(phi) - (y[0] ** 2 / a) * np.tan(phi)
            dw_dt = 2 * omega * y[0] * np.cos(phi) + (y[0] ** 2 / a)
            dx_dt = y[0]  # u
            dy_dt = y[1]  # v
            dz_dt = y[2]  # w
            return [du_dt, dv_dt, dw_dt, dx_dt, dy_dt, dz_dt]

        # Time domain for integration
        t_span = (0, t)
        t_eval = np.linspace(0, t, 1000)

        # Solve the ODE system
        solution = solve_ivp(ode_system, t_span, initial_conditions, t_eval=t_eval, method='RK45')

        if not solution.success:
            messagebox.showerror('Error', 'ODE solver failed.')
            return

        # Extract the solution variables
        #u = solution.y[0]
        #v = solution.y[1]
        #w = solution.y[2]
        x = solution.y[3]
        y_pos = solution.y[4]  # To distinguish from vector solution y
        z = solution.y[5]

        # We add the curves to the graph
        self._add_curve(x, y_pos, z)

    def reset(self):
        """
        Clears the plot
        :return:
        """

        # Clear axes
        self.ax.clear()
        self.curves = []
        self.curve_count = 0
        self.canvas.draw()

if __name__ == "__main__":
    app = MomentumEquationsAstrophysicsApp()
    app.mainloop()