numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# with lambda
evenList = filter(lambda x: x % 2 == 0, numbers)
print(list(evenList))

# without lambda
def evenNumbers(x):
    return x % 2 == 0
evenList = filter(evenNumbers, numbers)
print(list(evenList))