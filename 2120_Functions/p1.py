def sumAll(limitTo):
    total = 0
    for i in range(0, limitTo + 1):
        total += i
    return total

def sumAllSquares(limitTo):
    total = 0
    for i in range(limitTo + 1):
        total += i * i
    return total

if __name__ == '__main__':
    print(sumAll(100))
    print(sumAllSquares(3))