import tkinter as tk
vista = tk.Tk()
vista.title("Notaria x")
vista.geometry("800x500+60+20")
vista.resizable(False,False)
# vista.minsize(800,500)
# vista.maxsize(900,600)
# esta va si tienes ya un icono desde antes o en la misma carpeta del proyecto
# vista.iconbitmap("nombreicono.ico")
vista.configure(bg="ivory3")
# elementos
frame1 = tk.Frame(vista)
frame1.configure(width=500, height=400, bg="red", bd=3)
frame2 = tk.Frame(frame1)
frame2.configure(width=200, height=200, bg="green", bd=3)
frame1.pack()
frame2.pack()
btn = tk.Button(frame1, text="Hello World")
btn.pack()

label = tk.Label(vista, text="estoy dentro de vista",bg="orange", padx=10,pady=20).pack()


vista.mainloop()