import random
import math

def leer_numero(ini, fin, mensaje):
    itsOK = False
    while itsOK == False:
        n = input(mensaje)
        try:
            ini = int(ini)
            fin = int(fin)
            n = int(n)
            if n >= ini and n <= fin:
                itsOK = True
        except:
            pass
    return n           

def generador():
    numeros = leer_numero(1, 20, "¿Cuantos números quieres generar? [1-20]:")
    modo = leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")
    l = []
    for i in range(numeros):
        n = random.uniform(0,101)
        if modo == 1:
            r = math.ceil(n)
            print("Num: {} -> round: {}".format(n, r))
        elif modo == 2:
            r = math.floor(n)
            print("Num: {} -> round: {}".format(n, r))
        elif modo == 3:
            r = round(n)
            print("Num: {} -> round: {}".format(n, r))
        
        l.append(r)
    return l   


print(generador())
        