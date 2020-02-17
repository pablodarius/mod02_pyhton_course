from functools import reduce

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# with lambda
sumAll = reduce(lambda x, y: x + y, numbers)
print(sumAll)
sum100 = reduce(lambda x, y: x + y, range(101))
print(sum100)

# with lambda
def sum(x, y):
    return x + y
sumAll = reduce(sum, numbers)
print(sumAll)