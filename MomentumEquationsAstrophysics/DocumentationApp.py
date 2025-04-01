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

Documentation_window = Tk()
Documentation_window.title("Documentation")
Documentation_window.iconbitmap('US-marca-principal.ico')
Documentation_window.geometry("640x480")  # Establecer tamaño de la nueva ventana
Documentation_window.resizable(False, False)

# Agregar texto
label = Label(Documentation_window, text="DOCUMENTATION FOR MOMENTUM EQUATIONS IN ASTROPHYSICS")
label.pack(padx=10, pady=10)

# Create a scrollbar for fucntionalities
scrollbar = Scrollbar(Documentation_window)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the text in functionalities
functext = Text(Documentation_window, height=50, yscrollcommand=scrollbar.set)
functext.pack(padx=10, pady=10, fill='both', expand=True)

# Open and read file
funcopen = open('AstroDocumentation.txt', 'r')
funcread = funcopen.read()
functext.insert(END, funcread)
funcopen.close()
scrollbar.config(command=functext.yview)

Documentation_window.mainloop()