import sqlite3

# conexion y se creara si no existe la BBDD
conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

"""
cursor.execute('''
    CREATE TABLE usuarios (
        dni VARCHAR(9) PRIMARY KEY,
        nombre VARCHAR(100),
        edad INTEGER,
        email VARCHAR(100)
    )
    ''')

usuarios = [
    ("0000000A", 'Ana', 33, 'afrodita@gmail.com'),
    ("11111111B", 'Lucas', 5, 'lucas@gmail.com'),
    ("22222222C", 'Marina', 3, 'marina@gmail.com'),
    ("33333333D", 'Pablo', 34, 'pablo@gmail.com')
]

cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)


cursor.execute('''
    CREATE TABLE productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100) NOT NULL,
        marca VARCHAR(100) NOT NULL,
        precio FLOAT NOT NULL
    )
    ''')

productos = [
    ('Teclado', 'Logitec', 19.95),
    ('Pantallaa 19"', 'LG', 89.95),
    
]

cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
"""

cursor.execute("SELECT * FROM productos")

prods = cursor.fetchall()
for p in prods:
    print(p)


cursor.execute('''
    CREATE TABLE personas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dni VARCHAR(9) UNIQUE,
        nombre VARCHAR(100),
        edad INTEGER,
        email VARCHAR(100)
    )
    ''')

usuarios = [
    ("0000000A", 'Ana', 33, 'afrodita@gmail.com'),
    ("11111111B", 'Lucas', 5, 'lucas@gmail.com'),
    ("22222222C", 'Marina', 3, 'marina@gmail.com'),
    ("33333333D", 'Pablo', 34, 'pablo@gmail.com')
]

cursor.executemany("INSERT INTO personas VALUES (null,?,?,?,?)", usuarios)



conexion.commit()
conexion.close()