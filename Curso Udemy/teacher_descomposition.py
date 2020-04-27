import sys

errorMessage = "Sorry, something went wrong. Please Try again (execute with one argument, not negative integer)"

if len(sys.argv) == 2:
    number = int(sys.argv[1])    
    if number < 0 or number > 9999:
        print(errorMessage)
    else:
        cadena = str(number)
        long = len(cadena)

        for i in range(long):
            print("{:04d}".format(int(cadena[long-1-i]) * 10 ** i))        
else:
    print(errorMessage)