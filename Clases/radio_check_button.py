import tkinter as tk
ventana =tk.Tk()
ventana.title("Check y raddio button")

# radiobuttons
variableControl = tk.IntVar()
btnControl = tk.IntVar()
chControl = tk.BooleanVar()
# funciones
def mostrarEleccion():
    print("btn seleccionado", btnControl.get())

def cambiarColor():
    color_seleccionado = variableControl.get()
    if color_seleccionado == 1:
        ventana.config(bg="red")
    elif color_seleccionado == 2:
        ventana.config(bg="blue")

def onCheckButton():
    if chControl.get():
        btnCheck.config(state="normal")
    else:
        btnCheck.config(state="disabled")


# elementos
# ejemplo
# radiobtn = tk.Radiobutton(ventana, text="opcion1", font=("arial",22),bg="lightgray",fg="blue")
# radiobtn.pack()


opcion1 = tk.Radiobutton(ventana, text= "opcion1", variable= btnControl, value = 1)
opcion2 = tk.Radiobutton(ventana, text= "opcion2", variable= btnControl, value = 2)
opcion1.pack()
opcion2.pack()


opcionColor1 = tk.Radiobutton(ventana, text= "rojo", variable= variableControl, value = 1, command=cambiarColor)
opcionColor2 = tk.Radiobutton(ventana, text= "azul", variable= variableControl, value = 2, command=cambiarColor)
btnMostrar = tk.Button(ventana, text="mostrar eleccion", command=mostrarEleccion)
btnMostrar.pack()
opcionColor1.pack()
opcionColor2.pack()




# checkbuttons
variableCheck1 = tk.Checkbutton()
variableCheck2 = tk.Checkbutton()
variableCheck3 = tk.Checkbutton()

check1 = tk.Checkbutton(ventana, text= "check1", font=("arial",20),fg="red", variable= variableCheck1, command=onCheckButton)
check1.pack()
check2 = tk.Checkbutton(ventana, text= "check2", font=("arial",20),fg="green", variable=variableCheck2, command=onCheckButton)
check2.pack()
check3 = tk.Checkbutton(ventana, text= "check3",variable=chControl, command=onCheckButton)
check3.pack()
btnCheck = tk.Button(ventana, text="Hola", state="disabled")
btnCheck.pack()

ventana.mainloop()