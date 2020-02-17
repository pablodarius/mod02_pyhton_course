numbers = (1, 3, -1, 15, 9)

# with lambda
listDoble = map(lambda x: x*2, numbers)
print(list(listDoble))

# without lambda
def dobleNumber(x):
    return x*2
listDoble = map(dobleNumber, numbers)
print(list(listDoble))