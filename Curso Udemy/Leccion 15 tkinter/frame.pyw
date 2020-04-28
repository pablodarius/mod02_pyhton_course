from tkinter import *

root = Tk()

root.title("Hola mundo")
root.resizable(1,1)
root.iconbitmap("hola.ico")

frame = Frame(root, width=480, height=320)
# frame.pack() # alinea arriba y al medio por defecto
# frame.pack(side="bottom", anchor="e") # e de east (north, south east west)
frame.pack(fill='both', expand=1) # x, y o both
frame.config(cursor="pirate")
frame.config(bg="lightBlue")
frame.config(bd=20)
frame.config(relief="sunken")


root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")

# abajo del todo
root.mainloop()
