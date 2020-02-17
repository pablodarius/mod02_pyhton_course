def maxNum(*l):
    if len(l) == 0:
        return 0
    item = l[0]
    for i in range(1, len(l)):
        if l[i] > item:
            item = l[i]
    return item

def minNum(*l):
    if len(l) == 0:
        return 0
    item = l[0]
    for i in range(1, len(l)):
        if l[i] < item:
            item = l[i]
    return item

def arithMean(*l):
    if len(l) == 0:
        return 0
    sum = 0
    for i in l:
        sum += i
    return sum/len(l)

functions = {
    'max': maxNum,
    'min': minNum,
    'mean': arithMean
}

def returnFunction(name):
    name = name.lower()
    if name in functions.keys():
        return functions[name]
    return None

print(maxNum(9,10,3,4,5,6,7,8,1,2,2,3))
print(minNum(9,10,3,4,5,6,-7,8,-1,2,2,3))
print(arithMean(3,3))
print(returnFunction('max')(4,5,6,7,8,4,6,5,7,88,7,65))
print(returnFunction('min')(4,5,6,7,-8,4,6,5,7,88,7,65))
print(returnFunction('mean')(4,5,6))