import sqlite3

# conexion y se creara si no existe la BBDD
conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()

# cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INT, email VARCHAR(100))")
# cursor.execute( "INSERT INTO usuarios VALUES ('Pablo',34,'myemail@gmail.com')" )
# cursor.execute( "SELECT * FROM usuarios" )
# usu = cursor.fetchone() # recupera el primero en forma de tupla, no se puede modificar
# print(usu)
# print(usu[0])
"""
usuarios = [
    ('Ana', 33, 'afrodita@gmail.com'),
    ('Lucas', 5, 'lucas@gmail.com'),
    ('Marina', 3, 'marina@gmail.com')
]

cursor.executemany( "INSERT INTO usuarios VALUES (?,?,?)", usuarios )
"""

cursor.execute( "SELECT * FROM usuarios" )
usuarios = cursor.fetchall() # recupera el primero en forma de tupla, no se puede modificar

for u in usuarios:
    print(u[0], u[1], u[-1])

conexion.commit()
conexion.close()