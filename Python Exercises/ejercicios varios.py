# Ejercicio 6.1. Escribir un ciclo que permita mostrar los caracteres de una cadena del final al principio.
word = "cagadutaz"
wordRev = ""
for l in range(len(word)-1, -1, -1):
    wordRev += word[l]

print(wordRev)
#########################################################

counterA = 0
counterE = 0
counterI = 0
counterO = 0
counterU = 0
for l in word:
    if l.upper() == 'A':
        counterA += 1
    elif l.upper() == 'E':
        counterE += 1
    elif l.upper() == 'I':
        counterI += 1
    elif l.upper() == 'O':
        counterO += 1
    elif l.upper() == 'U':
        counterU += 1
print([counterA, counterE, counterI, counterO, counterU])