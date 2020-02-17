def normal(x):
    return x

def square(x):
    return x * x

def cube(x):
    return x**3

def sumAll(limitTo, f):
    result = 0
    for i in range(limitTo +1):
        result += f(i)
    return result

if __name__ == '__main__':
    print(sumAll(100, normal))
    print(sumAll(3, square))
    print(sumAll(3, cube))
