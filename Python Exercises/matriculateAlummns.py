# añadir dni para matriicular gente a una lista, poder borrar si ya está
import sys
import unittest

finish = False
matriculatedAlumns = []
while not finish:
    dni = input("Please, introduce DNI of the alumn (empty for exit): ")
    try:        
        if dni == '':
            finish = True
        elif int(dni) > 0 and dni not in matriculatedAlumns:
            matriculatedAlumns.append(dni)
    except ValueError as e:
        print(F"Invalid intro: {e}")
print(matriculatedAlumns)

def eliminateMatriculated(dniToEliminate):
    matriculatedAlumns.remove(dniToEliminate)

eliminateMatriculated('1')
eliminateMatriculated('3')
print(matriculatedAlumns)


'''
if __name__ == "__main__":
    unittest.main()
'''