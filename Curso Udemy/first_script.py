import sys
if len(sys.argv) == 3:        
    print("Hi, this is the first script.")

    text = sys.argv[1]
    rep = int(sys.argv[2])

    for r in range(rep):
        print(text)
else:
    print("Error, wrong args.")