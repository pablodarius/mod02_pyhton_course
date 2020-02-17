from functionsFirstLevel import sumAll

doble = lambda x: x*2
triple = lambda x: x*3

print(sumAll(3, lambda x: x**3))
print(sumAll(3, doble))
print(sumAll(3, triple))
