from tkinter import*
import tkinter as tk

base= tk.Tk()

# --> Diseño ventana principal
base.title("Entorno Simulación Coche Autónomo")
base.resizable(0,0)
base.iconbitmap("coche.ico")
base.geometry("650x720")
base.config(bg="#3092CE", bd="20")

# --> Botón Empezar
botonEmpezar = tk.Button(base, text="Empezar Simulación")
botonEmpezar.config(fg="#FF8837", font=("Century Gothic", 18, 'bold'))
botonEmpezar.grid(row=13, column=1, pady=70)







