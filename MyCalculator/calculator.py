from tkinter import *
from tkinter import ttk

class Calculator(Tk):    
    size = "400x600"
    box = None
    btn = None
    
    def __init__(self):
        Tk.__init__(self)        
        self.geometry(self.size)
        self.title("Calculator")
        self.configure(bg="#DED798")
        self.resizable(0, 0)        
        self.box = StringVar(value="")
        
        self.createLayout()        

    def createLayout(self):
        contX=0
        contY=0
        conSings = 0
        bg = '#BDBDBD'
        fg = '#000000'
        relief = 'raised'
        font = "Helvetica 30 bold"

        self.input = Entry(self, textvariable=self.box, font=font, justify="right").place(x=0, y=0, width=400, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='C', command=lambda: self.pushBtn('C')).place(x=0, y=101, width=200, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='%', command=lambda: self.pushBtn('%')).place(x=200, y=101, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='/', command=lambda: self.pushBtn('/')).place(x=300, y=101, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='0', command=lambda: self.pushBtn('0')).place(x=0, y=501, width=200, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='.', command=lambda: self.pushBtn('.')).place(x=200, y=501, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='=', command=lambda: self.pushBtn('=')).place(x=300, y=501, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='7', command=lambda: self.pushBtn('7')).place(x=0, y=201-contY, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='8', command=lambda: self.pushBtn('8')).place(x=100, y=201-contY, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='9', command=lambda: self.pushBtn('9')).place(x=200, y=201-contY, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='X', command=lambda: self.pushBtn('x')).place(x=300, y=201-contY, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='4', command=lambda: self.pushBtn('4')).place(x=0, y=301-contY, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='5', command=lambda: self.pushBtn('5')).place(x=100, y=301-contY, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='6', command=lambda: self.pushBtn('6')).place(x=200, y=301-contY, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='-', command=lambda: self.pushBtn('-')).place(x=300, y=301-contY, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='1', command=lambda: self.pushBtn('1')).place(x=0, y=401-contY, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='2', command=lambda: self.pushBtn('2')).place(x=100, y=401-contY, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='3', command=lambda: self.pushBtn('3')).place(x=200, y=401-contY, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='+', command=lambda: self.pushBtn('+')).place(x=300, y=401-contY, width=100, height=100)

    
    def pushBtn(self, txt=""):
        if txt == 'C':
            self.box.set("")
        else:
            label = self.box.get()
            label = label + str(txt)
            self.box.set(label)
      

    def start(self):
        self.mainloop()