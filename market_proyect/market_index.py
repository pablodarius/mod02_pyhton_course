from tkinter import *
import connection

def mostrar_menu_cartel():
    s = "SELECT * FROM MARKET"
    markets = connection.executeSelect(s)  
    for m in markets:        
        Button(frame, text=m[1], font=("Castellar 18"), bg="#617996", command=lambda: pulseButton(name)).pack(anchor="n")        

def mainPage():
    Button(frame, text='MARKETS', font=("Castellar 18"), bg="#617996", command=markets()).place(width=242.5, height=100)
    Button(frame, text='PRODUCTS', font=("Castellar 18"), bg="#617996", command="").place(x=242.5,width=242.5, height=100)
    Button(frame, text='CART', font=("Castellar 18"), bg="#617996", command="").place(y=101,width=242.5, height=100)
    Button(frame, text='HISTORICAL', font=("Castellar 18"), bg="#617996", command="").place(x=242.5,y=101,width=242.5, height=100)
    Button(frame, text='EXIT', font=("Castellar 18"), bg="#617996", command=quit).place(y=202,width=485, height=100)

def markets():
    frame.destroy    
    

root = Tk()

root.title("The Frying Dutchman")
root.resizable(0,0)
root.iconbitmap("./images/dino.ico")
imagen = PhotoImage(file="./images/bar.png")
Label(root, image=imagen).pack( side="top")
frame = Frame(root, width=512, height=600)

frame.pack(fill='both', expand=1) # x, y o both
frame.config(bg="#617996")
frame.config(bd=20)
frame.config(relief="sunken")

# Label(frame, text="The Frying Dutchman Menu", font=("Broadway 20 bold"), bg="#617996").pack(anchor="n")

mainPage()
# mostrar_menu_cartel()

# Label(frame, text="\n12€ (TAX INCLUDED)", font=("Castellar 18 bold"), fg="#cc0001", bg="#617996").pack(anchor="e")

# abajo del todo
root.mainloop()