import tkinter as tk
ventana = tk.Tk()
# ejemplo de grid
# label1 = tk.Label(ventana, text="Hola")
# label2 = tk.Label(ventana, text="Hola2")
# label1.grid(row =0, column =0, padx = 100, pady=100)
# label2.grid(row =1, column =1, padx = 100, pady=100)
#--------------------------------------------------------------
# label1 = tk.Label(ventana, text="celda 1.1")
# label2 = tk.Label(ventana, text="celda 1.2")
# label3 = tk.Label(ventana, text="celda 2.1")
# label4 = tk.Label(ventana, text="celda 2.2")
# label1.grid(row =0, column =0, padx = 5, pady=5)
# label2.grid(row =0, column =1, padx = 5, pady=5)
# label3.grid(row =1, column =0, padx = 5, pady=5)
# label4.grid(row =1, column =1, padx = 5, pady=5)

# ejemplo de pack
frame_btn = tk.Frame(ventana)
frame_btn.pack(pady=10)

btn1 = tk.Button(frame_btn, text="btn1")
btn2 = tk.Button(frame_btn, text="btn2")
btn3 = tk.Button(frame_btn, text="btn3  ")
btn1.pack(side="left", padx =5)
btn2.pack(side="left", padx =5)
btn3.pack(side="left", padx =5)

ventana.mainloop()