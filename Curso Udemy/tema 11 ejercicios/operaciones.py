typeErr = "Error: Tipo de dato no válido"
ZeroErr = "Error: No es posible dividir entre cero"

def suma(a,b):
    try:        
        return a + b
    except TypeError:
        print(typeErr)
    

def resta(a,b):
    try:        
        return a - b
    except TypeError:
        print(typeErr)

def producto(a,b):
    try:        
        return a * b
    except TypeError:
        print(typeErr)

def division(a,b):
    try:        
        return a / b
    except TypeError:
        print(typeErr)
    except ZeroDivisionError:
        print(ZeroErr)