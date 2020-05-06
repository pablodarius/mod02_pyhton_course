import sqlite3
from tkinter import *

def crear_bd():
    # conexion y se creara si no existe la BBDD
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            CREATE TABLE categoria(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre VARCHAR(100) UNIQUE NOT NULL)
        """)
        conexion.commit()
    except Exception as e:
        print("Error al crear la table categoria:", e)

    try:
        cursor.execute("""
            CREATE TABLE plato(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre VARCHAR(100) UNIQUE NOT NULL, 
				categoria_id INTEGER NOT NULL,
				FOREIGN KEY(categoria_id) REFERENCES categoria(id))
        """)
        conexion.commit()
    except Exception as e:
        print("Error al crear la table plato:", e)
    
    conexion.close()

def agregar_categoria():
    # conexion y se creara si no existe la BBDD
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    category = input("Introduce el nombre de una nueva categoría: ")

    try:        
        cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(category))
        conexion.commit()
    except Exception as e:
        print("Error al crear la categoría:", e)
    
    conexion.close()

def agregar_plato():
    # conexion y se creara si no existe la BBDD
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    cursor.execute( "SELECT * FROM categoria" )
    categories = cursor.fetchall()
    ids = []
    for c in categories:
        print("{}.- {}".format(c[0], c[1]))
        ids.append(c[0])

    idCategory = int(input("Introduce el número de una categroía para el nuevo plato: "))
    if idCategory in ids:
        plate = input("Introduce el nombre del nuevo plato: ")
        try:        
            cursor.execute("INSERT INTO plato VALUES (null, '{}', '{}')".format(plate, idCategory))
            conexion.commit()
        except Exception as e:
            print("Error al crear el plato:", e)
    else:
        print("No existe ese id de categoría.")    
    
    conexion.close()

def mostrar_menu():
    # conexion y se creara si no existe la BBDD
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    cursor.execute( "SELECT * FROM categoria" )
    categories = cursor.fetchall()

    for c in categories:
        print(c[1])
        cursor.execute( "SELECT * FROM plato where categoria_id = {}".format(c[0]) )
        plates = cursor.fetchall()       
        for p in plates:
            print("\t- {}".format(p[1]))            
    
    conexion.close()

def mostrar_menu_cartel():
    # conexion y se creara si no existe la BBDD
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    cursor.execute( "SELECT * FROM categoria" )
    categories = cursor.fetchall()

    for c in categories:
        Label(frame, text="\n"+c[1], font=("Castellar 18 bold"), bg="#617996").pack(anchor="n")       
        cursor.execute( "SELECT * FROM plato where categoria_id = {}".format(c[0]) )
        plates = cursor.fetchall()       
        for p in plates:
            Label(frame, text=p[1], font=("Castellar 18"), bg="#617996").pack(anchor="n")               

    conexion.close()

crear_bd()
"""agregar_categoria()
agregar_categoria()
agregar_categoria()
agregar_plato()
agregar_plato()
agregar_plato()
agregar_plato()
agregar_plato()
agregar_plato()
agregar_plato()
mostrar_menu()"""

root = Tk()

root.title("The Frying Dutchman")
root.resizable(0,0)
imagen = PhotoImage(file="bar.png")
Label(root, image=imagen).pack( side="top")
frame = Frame(root, width=512, height=600)

frame.pack(fill='both', expand=1) # x, y o both
frame.config(bg="#617996")
frame.config(bd=20)
frame.config(relief="sunken")

Label(frame, text="The Frying Dutchman Menu", font=("Broadway 20 bold"), bg="#617996").pack(anchor="n")
Label(frame, text="\nToday´s Menu", font=("Castellar 22 bold"), bg="#617996").pack(anchor="n")

mostrar_menu_cartel()

Label(frame, text="\n12€ (TAX INCLUDED)", font=("Castellar 18 bold"), fg="#cc0001", bg="#617996").pack(anchor="e")


# abajo del todo
root.mainloop()