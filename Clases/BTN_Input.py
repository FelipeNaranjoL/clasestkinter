import time
import tkinter as tk
# caracteristicas de la ventana
ventana = tk.Tk()
ventana.title("Clase 2")
# variables
# widgets
label = tk.Label(ventana,text = "Hello World")
# label.config(fg="red", bg="green", font=("arial",30, "bold"))
label.pack()
btn = tk.Button(ventana, text = "sos", fg="red",bg="blue", font=("arial",25,"bold"))
btn.pack()
label2 = tk.Label(ventana,text ="AA:EE:II")
label2.pack()
labelEntry = tk.Entry(ventana, bg="yellow", fg="red", font=("Arial",22,"bold"))
labelEntry.pack()
labelEntry.insert(0,"Text Example")
impresion = labelEntry.get()
print(impresion)
#funciones
def hora():
    label.config(text=time.strftime("%H:%M:%S"))
    ventana.after(1000, hora)
hora()

def presion():
    print("Pides auxilio")

def cambiarTexto():
    label2.config(text="pides auxilio")

btn.config(command=cambiarTexto)




ventana.mainloop()