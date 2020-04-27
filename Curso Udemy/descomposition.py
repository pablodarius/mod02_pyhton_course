import sys

errorMessage = "Sorry, something went wrong. Please Try again (execute with one argument, not negative integer)"

if len(sys.argv) == 2:
    number = int(sys.argv[1])
    strNumber = str(sys.argv[1])
    size = len(sys.argv[1])
    string = ''
    count = size -1
    if number >= 0:
        for c in range(0, size):
             string += '0'
        for i in range(size-1, -1, -1):           
            d = strNumber[i]
            if d != '0':
                aux = list(string)
                aux[count] = d   
                aux = ''.join(aux)          
                count -= 1
                print(aux)
    else:
        print(errorMessage)
else:
    print(errorMessage)