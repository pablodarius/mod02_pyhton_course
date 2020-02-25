import turtle
import random
import tkinter
from tkinter import messagebox

class Circuit():
    runners = []
    __posStartY = (-30, -10, 10, 30)
    __turtleColor = ('red','blue','green','orange')
    
    def __init__(self, width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor("lightgrey")
        self.__startLine = -width/2 + 20
        self.__finishLine = width/2 - 20

        self.createRunners()
    
    def createRunners(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__turtleColor[i])
            new_turtle.shape("turtle")            
            new_turtle.penup()
            new_turtle.setpos(self.__startLine, self.__posStartY[i])

            self.runners.append(new_turtle)
    
    def startRace(self):
        winner = False
        # turtleWinner = ''
        while not winner:
            for turtle in self.runners:
                run = random.randint(1,12)
                turtle.forward(run)
                
                if turtle.position()[0] >= self.__finishLine:
                    winner = True
                    messagebox.showinfo("And The WINNER Is...", turtle.color()[0])
                    print("And the winner is the {} turtle".format(turtle.color()[0]))
                    break
                    
            
        



if __name__ == "__main__":
    daytona = Circuit(640, 480)
    print(daytona)
    daytona.startRace()
