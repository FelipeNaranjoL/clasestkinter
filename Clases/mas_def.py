import tkinter as tk
ventana = tk.Tk()
#funciones
def on_click(event):
    print("btn presionado")

def key_press(event):
    if event.char =="a":
        print("a presionada")

def on_resize (event):
    print(f"se ha modificado el tamaño de la ventana {event.width} x {event.height}")

def on_mouse (event):
    print(f"se movio el mouse {event.x} x {event.y}")

def on_click2 (event):
    print(f"boton {event.widget['text']} presionado")

btn = tk.Button(ventana, text="Hola mundo")
btn.pack()
btn.bind("<Button-1>", on_click)
btns = [tk.Button(ventana, text=f"Hola Mundo {i}") for i in range(3)]
for button in btns:
    button.pack()
    button.bind("<Button-1>", on_click2)


ventana.bind("<KeyPress>", key_press)
ventana.bind("<Configure>", on_resize)
ventana.bind("<Motion>", on_mouse)
#"<Button-1>" = click izquierdo del mouse





ventana.mainloop()