from tkinter import *

root = Tk()
root.config(bd=15)

"""
def hola():
    print("Hola Mundo");

def crear_label():
    Label(root, text="Label creada dinámicamente").pack()

Button(root, text="Clickame", command=crear_label).pack() # la funcion crear_label debe estar declarada antes
"""

def sumar():
    res.set(float(n1.get()) + float(n2.get()))
    borrar()

def resta():
    res.set(float(n1.get()) - float(n2.get()))
    borrar()

def producto():
    res.set(float(n1.get()) * float(n2.get()))
    borrar()

def borrar():
    n1.set('')
    n2.set('')

n1 = StringVar()
n2 = StringVar()
res = StringVar()

Label(root, text="Número 1:").pack()
Entry(root, justify="center", textvariable=n1).pack() # sumando 1
Label(root, text="Número 2:").pack()
Entry(root, justify="center", textvariable=n2).pack() # sumando 2
Label(root, text="Resultado:").pack()
Entry(root, justify="center", textvariable=res, state="disabled").pack() # resultado
Label(root, text="").pack()
Button(root, text="Sumar", command=sumar).pack(side="left")
Button(root, text="Resta", command=resta).pack(side="left")
Button(root, text="Producto", command=producto).pack(side="left")


# abajo del todo
root.mainloop()