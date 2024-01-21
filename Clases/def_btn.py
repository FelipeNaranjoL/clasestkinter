import tkinter as tk
import time
ventana = tk.Tk()

label = tk.Label(ventana,text="Ingresa tu nombre")
label.pack()
labelEntry = tk.Entry(ventana, bg="#00ff00", fg="red")
labelEntry.pack()
labelEntry.insert(0,"Ingresar nombre")

def ingresarDato():
    texto= labelEntry.get()
    label.config(text=texto)

labelBtn = tk.Button(ventana, text="Ingresar", command=ingresarDato)
labelBtn.pack()






ventana.mainloop()