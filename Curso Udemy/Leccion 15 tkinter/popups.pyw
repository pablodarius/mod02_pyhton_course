from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

root = Tk()

def test():
    # MessageBox.showinfo("Hola","Hola Mundo")
    # MessageBox.showwarning("Alerta","Sección solo para administradores")
    # MessageBox.showerror("Error","Ha ocurrido un error")
    # respuesta = MessageBox.askquestion("Salir","¿Estás seguro?")
    # if respuesta == "yes": # no
    #    root.destroy()
    # respuesta = MessageBox.askokcancel("Salir","¿Quiéres sobreescribir?")
    # if respuesta == True: # False
    #    root.destroy()
    # respuesta = MessageBox.askyesno("Salir","¿Quiéres salir?")
    # if respuesta == True: # False
    #    root.destroy()
    # respuesta = MessageBox.askretrycancel("Salir","¿Quiéres volverlo a intentar?")
    # if respuesta == True: # False
    #    root.destroy()
    # color = ColorChooser.askcolor(title="Elige un color")
    # print(color) # devuelve tupla, primero el código rgb en tuple de 3 y después en hexadecimal. si cancelar devuelve tuple conm None y None
    """ruta = FileDialog.askopenfilename(title="Abrir un fichero", initialdir="C:", filetypes=(("Ficheros de texto", "*.txt"),
                                                                                            ("Ficheros de texto avanzado", "*.txt2"),
                                                                                            ("Todos los Ficheros", "*.*")) ) # si cancelar, devuelve cadena vacía
    print(ruta)"""
    # devuelve un fichero ya abierto. equivale por defecto a open('ruta', 'W'), lo vacia al abrir
    fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode="a+", defaultextension=".txt") # se puede elegir el modo por parametros
    print(fichero) # cancelar devuelve none
    if fichero is not None:
        fichero.write("Hola")
        fichero.close()

Button(root, text="Clickame", command=test).pack()

# abajo del todo
root.mainloop()