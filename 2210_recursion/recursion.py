number = 10

def backCounter(n):
    if n != 0:
        print("{},".format(n))
        backCounter(n-1)
    else:
        print(0)    

print("---- Back Counter: {} ----".format(number))
backCounter(number)

def sum(n):
    if n > 0:
        return n + sum(n-1)
    else:
        return 0

number = 10
print("---- Summation ----")
print("{} => {}".format(number, sum(number)))

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

number = 8
print("---- Factorial ----")
print("{} => {}".format(number, factorial(number)))
    
