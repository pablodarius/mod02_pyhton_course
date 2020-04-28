from tkinter import *

root = Tk()
"""
frame = Frame(root)
frame.pack()
entry = Entry(frame)
entry.pack(side="right")
label = Label(frame, text="Nombre:")
label.pack(side="left")

frame1 = Frame(root)
frame1.pack()
entry1 = Entry(frame1)
entry1.pack(side="right")
label1 = Label(frame1, text="Apellidos:")
label1.pack(side="left")
"""
# mejor colocar con grid
label = Label(root, text="Nombre:")
label.grid(row=0, column=0, sticky="e", padx=5, pady=5) # sticky pega el label al este

entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5) # padding en ejes (x,y)
entry.config(justify="right", state="disabled")

label1 = Label(root, text="Contraseña de entrada:")
label1.grid(row=1, column=0, sticky="e", padx=5, pady=5)

entry1 = Entry(root)
entry1.grid(row=1, column=1, padx=5, pady=5)
entry1.config(justify="center", show="*")


# abajo del todo
root.mainloop()