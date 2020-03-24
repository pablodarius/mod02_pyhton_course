from tkinter import *
from tkinter import ttk

class mainApp(Tk):    
    size = "200x150"
    temp = None
    unit = None

    __validateTemp = ''

    def __init__(self):
        Tk.__init__(self)        
#       self. root = Tk()
        self.geometry(self.size)
        self.title("Thermometer")
        self.configure(bg = "#DED798")
        self.resizable(0,0)

        self.temp = StringVar(value="")
        self.temp.trace('w', self.validateTemp)
        self.unit = StringVar(value="C")

        self.createLayout()
    
    def validateTemp(self, *args):
        newValidate = self.temp.get()
        try:
            float(newValidate)
            self.__validateTemp = newValidate
        except:
            self.temp.set(self.__validateTemp)      


    def createLayout(self):
       self.input = Entry(self, textvariable=self.temp).place(x=10, y=10)
       self.lblunit = Label(self, text="Grades").place(x=10, y=40)
       self.rbunitC = Radiobutton(self, text="Celsius", variable=self.unit, value='C', command=self.selected).place(x=20, y=110)
       self.rbunitF = Radiobutton(self, text="Farenheit", variable=self.unit, value='F', command=self.selected).place(x=20, y=80)       
    
    def selected(self, *args):
        result = 0
        toUnit = self.unit.get()
        grades = float(self.temp.get())
        if toUnit == "F":
            result = grades * 9/5 + 32
        elif toUnit == "C":
            result = (grades - 32) * 5/9
        else:
            result = grades
        self.temp.set(result)

    def start(self):
        self.mainloop()

if __name__ == '__main__':
    app = mainApp()
    app.start()