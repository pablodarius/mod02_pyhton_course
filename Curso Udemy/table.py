import sys

errorMessage = "Sorry, something went wrong. Please Try again (execute with two arguments, integers between 1 and 9)"

if len(sys.argv) == 3:
    rows = int(sys.argv[1])
    columns = int(sys.argv[2])
    if (rows >= 1 and rows <= 9) and (columns >= 1 and columns <= 9):
        for r in range(rows):       
            print("")     
            for c in range(columns):
                print(" * ", end='')            
    else:
        print(errorMessage)
else:
    print(errorMessage)