import sys
from io import open
    
file = open("contador.txt", "a+") # append lectura y escritura, si no existe lo crea
file.seek(0) # el modo append deja el fichero al final
cont = file.read()
if cont == '':
    file.write('0')
    cont = '0'
file.close()
 
try:
    cont= int(cont)

    if len(sys.argv) == 2:
        if sys.argv[1] == 'inc':           
            cont += 1            
        elif sys.argv[1] == 'dec':            
            cont -= 1           
        print(cont)
        file = open("contador.txt", "w") # borra al abrirlo
        file.write(str(cont))
        file.close()
except:
    print("Error: corrupted file")