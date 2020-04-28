from tkinter import *

root = Tk()

# Variables dinámicas
texto = StringVar()
texto.set("Un nuevo texto")

#frame = Frame(root, width=480, height=320)
# frame.pack() # alinea arriba y al medio por defecto


#label = Label(frame, text="Hola mundo")
# label.pack()
# label = Label(root, text="Hola mundo")
# label.place(x=0, y=0)
# label.place(x=500, y=500)
# label.pack()

Label(root, text="Hola mundo").pack(anchor="nw") # si no vamos a usar la variable label podemos hacerlo todo a la vez
# Label(root, text="otra etiqueta").pack(anchor="center")
label = Label(root, text="otra etiqueta")
label.pack(anchor="center")
Label(root, text="Última etiqueta").pack(anchor="se")

label.config(bg="green", fg="blue", font=("Verdana",24))
label.config(textvariable=texto)

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack(side="left")

# abajo del todo
root.mainloop()
