from io import open
from tkinter import *
from tkinter import filedialog as FileDialog


ruta = "" # variable global para almacenar la ruta de un fichero

def new_file():
    global ruta # declaración de variable global
    mensaje.set("New file")
    ruta = ""
    texto.delete(1.0, "end") # borra desde el caracter 1.0 (el 0.0 que es un salto de línea siempre así que lo conservamos) hasta el final
    root.title("My Editor")

def open_file():
    global ruta
    mensaje.set("Open file")
    ruta = FileDialog.askopenfilename( initialdir='.', 
                                        filetypes=(("Text files", "*.txt"),),  
                                        title="Open text file" )                                     
    if ruta != "":
        file = open(ruta,"r")
        text = file.read()
        texto.delete(1.0, "end")
        texto.insert("insert", text)
        file.close()
        root.title(ruta + " - My Editor")


def save_file():
    global ruta
    mensaje.set("Save file")
    if ruta != "":
        text = texto.get(1.0, "end-1c") # el -1c es para no recuperar el último caracter tampoco que es un salto de línea
        file = open(ruta,"w+")
        file.write(text)
        file.close()
        mensaje.set("File saved, OK!")
    else:
        save_as_file()

def save_as_file():
    global ruta
    mensaje.set("Save as ...")
    file = FileDialog.asksaveasfile(title="Save file", mode="w", defaultextension="txt")
    if file is not None:
        ruta = file.name
        text = texto.get(1.0, "end-1c")
        file = open(ruta,"w+")
        file.write(text)
        file.close()
        mensaje.set("File saved, OK!")
    else:
        mensaje.set("Cancelling...!")


root = Tk()
root.title("My Editor")

# Menu superior
menubar = Menu(root)
filemenu= Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Save as", command=save_as_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(menu=filemenu, label="File")

# caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

# monitor inferior
mensaje = StringVar()
mensaje.set("Wellcome to the Editor")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")

root.config(menu=menubar)
# abajo del todo
root.mainloop()