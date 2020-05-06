import sqlite3

# conexion y se creara si no existe la BBDD
conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()
"""
cursor.execute("SELECT * FROM personas WHERE id=1")
per = cursor.fetchone()
print(per)
"""
cursor.execute("SELECT * FROM personas WHERE edad=34")
per = cursor.fetchone()
print(per)
per = cursor.fetchone()
print(per)
cursor.execute("SELECT * FROM personas WHERE edad=34")
perso = cursor.fetchall()
print(perso)


cursor.execute("UPDATE personas SET nombre='Pablo Pantoja' WHERE nombre='Pablo'")
cursor.execute("DELETE FROM personas WHERE nombre='Pablo Pantoja'")

conexion.commit()
conexion.close()