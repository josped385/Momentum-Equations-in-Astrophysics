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

Help_window = Tk()
Help_window.title("Help")
Help_window.iconbitmap('US-marca-principal.ico')
Help_window.geometry("903x668")  # Establecer tamaño de la nueva ventana
Help_window.resizable(False, False)

# Agregar texto
label = Label(Help_window, text="HELP FOR MOMENTUM EQUATIONS IN ASTROPHYSICS")
label.pack(padx=10, pady=10)

# Cargar y redimensionar la imagen de las ecuaciones del momento
MomentumPhoto = Image.open("problema7.png")  # Cambia por la ruta de tu imagen
MomentumPhoto_resized = MomentumPhoto.resize((450, 221))  # Cambia el tamaño (ancho, alto)
MomentumPhoto_photo = ImageTk.PhotoImage(MomentumPhoto_resized)
MomentumPhoto_label = Label(Help_window, image=MomentumPhoto_photo)
MomentumPhoto_label.pack(padx=10, pady=10)  # Cambia la posición (x, y)

# Create a scrollbar for fucntionalities
scrollbar = Scrollbar(Help_window)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the text in functionalities
functext = Text(Help_window, height=50, yscrollcommand=scrollbar.set)
functext.pack(padx=10, pady=10, fill='both', expand=True)

# Open and read file
funcopen = open('Helpfunctionalities.txt', 'r')
funcread = funcopen.read()
functext.insert(END, funcread)
funcopen.close()
scrollbar.config(command=functext.yview)

Help_window.mainloop()