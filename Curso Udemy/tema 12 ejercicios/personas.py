from io import open

file = open("personas.txt", "r", encoding="utf8")
lines = file.readlines()
file.close()

listPeople = []
for line in lines:
    line = line.replace("\n","").split(';')
    dictionary = {"id" : line[0], "nombre" : line[1], "apellido" : line[2], "nacimiento" : line[3]}
    listPeople.append(dictionary)

for p in listPeople:
    print("{}: {} {}, was born {}".format(p["id"], p["nombre"], p["apellido"], p["nacimiento"]))