from tkinter import *
from tkinter import ttk

class Calculator(Tk):    
    operators = ['+', '/', 'x', '*', '%']
    size = "400x600"
    box = None
    btn = None
        
    def __init__(self):
        Tk.__init__(self)        
        self.geometry(self.size)
        self.title("Calculator")
        self.configure(bg="#DED798")
        self.resizable(0, 0)        
        self.box = StringVar(value="0")
        
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
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='x', command=lambda: self.pushBtn('x')).place(x=300, y=201-contY, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='4', command=lambda: self.pushBtn('4')).place(x=0, y=301-contY, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='5', command=lambda: self.pushBtn('5')).place(x=100, y=301-contY, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='6', command=lambda: self.pushBtn('6')).place(x=200, y=301-contY, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='-', command=lambda: self.pushBtn('-')).place(x=300, y=301-contY, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='1', command=lambda: self.pushBtn('1')).place(x=0, y=401-contY, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='2', command=lambda: self.pushBtn('2')).place(x=100, y=401-contY, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='3', command=lambda: self.pushBtn('3')).place(x=200, y=401-contY, width=100, height=100)
        self.btn = Button(bg=bg, fg=fg, relief=relief, font=font, text='+', command=lambda: self.pushBtn('+')).place(x=300, y=401-contY, width=100, height=100)

    
    def pushBtn(self, txt=''):
        if txt == 'C':
            self.box.set('0')
        elif txt == '=':
            self.calculate()
        else:
            box = self.box.get()
            if (box == '0' or box == 'Error') and txt != '.':
                box = ''

            box = box + str(txt)
            self.box.set(box)
    
    def exeCalculate(self, op1, op2, sym):
        result = 0
        try:
            num1 = float(op1)
            num2 = float(op2)            
            if sym == '+': result = num1+num2
            elif sym == '-': result = num1-num2
            elif sym == 'x': result = num1*num2
            elif sym == '/': result = num1/num2
            elif sym == '%': result = num1%num2
            else: result = "Error"

            result = str(result)
        except:
            result = "Error"
                
        return result
    
    def calculate(self):        
        op1 = ''
        op2 = ''
        symbol = ''
        result = 0
        countMin = 0

        operation = self.box.get()
        lastChar = operation[-1:]

        if lastChar in self.operators:
            self.box.set("Error")
        
        for char in operation:
            if char == '-': countMin += 1
            if (countMin == 2 and symbol == '') or (char == '-' and op1 != '' and symbol == ''): 
                symbol = '-'
            else:
                if char not in self.operators:
                    if symbol == '':
                        op1 = op1 + char
                    else:
                        op2 = op2 + char
                else:
                    symbol = char

        result = self.exeCalculate(op1, op2, symbol)
        self.box.set(result)

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = Calculator()
    app.start()