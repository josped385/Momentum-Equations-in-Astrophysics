import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from nidaqmx import Task
from nidaqmx.constants import TerminalConfiguration
from nidaqmx.system import System
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog, ttk, simpledialog
from PIL import ImageTk, Image
from scipy.optimize import curve_fit
from scipy.integrate import solve_ivp
import pandas as pd
import csv
import threading

def CalculateAng():
    deg1 = float(Deg1.get())
    rad2 = float(Rad2.get())

    rad1 = deg1/180*np.pi
    deg2 = rad2*180/np.pi

    # Asignar resultados en el formato correcto
    Rad1.delete(0, tk.END)  # Limpiar el campo de entrada para radianes
    Deg2.delete(0, tk.END)  # Limpiar el campo de entrada para grados

    # Asignamos resultados
    Rad1.insert(0, f'{rad1: .7g}')
    Deg2.insert(0, f'{deg2: .7g}')

AngleCalculator_window = tk.Tk()
AngleCalculator_window.title("Angle Calculator")
AngleCalculator_window.iconbitmap('US-marca-principal.ico')
AngleCalculator_window.geometry("325x240")  # Establecer tamaño de la nueva ventana
AngleCalculator_window.resizable(False, False)

# Botón de calcular
Calculate = Button(AngleCalculator_window, text='Calculate', command=CalculateAng)
Calculate.grid(row=0, column=0, columnspan=10, padx=10, pady=10)

# Label con información de lo que hacen las primeras dos entrys
DegRad_label = Label(AngleCalculator_window, text='Degrees to radians calculator')
DegRad_label.grid(row=1, column=0, columnspan=10, padx=10, pady=10)

# Create label for Deg1
Deg1_label = Label(AngleCalculator_window, text="Degrees", padx=10, pady=5)
Deg1_label.grid(row=2, column=0, sticky="e", pady=10)

# Create the Deg1 Edit Field
Deg1default = IntVar()
Deg1default.set(0)
Deg1 = Entry(AngleCalculator_window, width=10, textvariable=Deg1default)
Deg1.grid(row=2, column=1, sticky="w", padx=5, pady=10)

# Label con flecha
Flecha_label = Label(AngleCalculator_window, text='->')
Flecha_label.grid(row=2, column=2, padx=10, pady=10)

# Create label for Rad1
Rad1_label = Label(AngleCalculator_window, text="Radians", padx=10, pady=5)
Rad1_label.grid(row=2, column=3, sticky="e", pady=10)

# Create the Rad1 Edit Field
Rad1default = IntVar()
Rad1default.set(0)
Rad1 = Entry(AngleCalculator_window, width=10, textvariable=Rad1default)
Rad1.grid(row=2, column=4, sticky="w", padx=5, pady=10)

# Label con información de lo que hacen las primeras dos entrys
RadDeg_label = Label(AngleCalculator_window, text='Radians to degrees calculator')
RadDeg_label.grid(row=3, column=0, columnspan=10, padx=10, pady=10)

# Create label for Deg2
Deg1_label = Label(AngleCalculator_window, text="Degrees", padx=10, pady=5)
Deg1_label.grid(row=4, column=3, sticky="e", pady=10)

# Create the Deg2 Edit Field
Deg2default = IntVar()
Deg2default.set(0)
Deg2 = Entry(AngleCalculator_window, width=10, textvariable=Deg2default)
Deg2.grid(row=4, column=4, sticky="w", padx=5, pady=10)

# Label con flecha
Flecha_label = Label(AngleCalculator_window, text='->')
Flecha_label.grid(row=4, column=2, padx=10, pady=10)

# Create label for Rad2
Rad2_label = Label(AngleCalculator_window, text="Radians", padx=10, pady=5)
Rad2_label.grid(row=4, column=0, sticky="e", pady=10)

# Create the Rad2 Edit Field
Rad2default = IntVar()
Rad2default.set(0)
Rad2 = Entry(AngleCalculator_window, width=10, textvariable=Rad2default)
Rad2.grid(row=4, column=1, sticky="w", padx=5, pady=10)

AngleCalculator_window.mainloop()