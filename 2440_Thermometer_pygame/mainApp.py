import pygame, sys
from pygame.locals import *

class Thermometer():
    def __init__(self):
        self.custome = pygame.image.load("./images/thermometer.png")

    def convert(self, grades, toUnit):
        result = 0
        if toUnit == "F":
            result = grades * 9/5 + 32
        elif toUnit == "C":
            result = (grades - 32) * 5/9
        else:
            result = grades

        return "{:10.2f}".format(result)

class Selector():
    __unit = None

    def __init__(self, unit= "C"):
        self.__customes = []
        self.__customes.append(pygame.image.load("./images/celsius.png"))
        self.__customes.append(pygame.image.load("./images/farenheit.png"))
        self.__unit = unit

    def getUnit(self):
        return self.__unit

    def getCustome(self):
        if self.__unit == "C":
            return self.__customes[0]
        elif self.__unit == "F":
            return self.__customes[1]
    
    def change(self):        
        if self.__unit == "C":
            self.__unit = "F"
        else:
            self.__unit = "C"


class NumberInput():
    __grades = 0
    __strValue = "0"
    __position = [0, 0]
    __size = [0, 0]
    __pointsCount = 0

    def __init__(self, grades=0):
        self.__font = pygame.font.SysFont("Arial", 24)
        self.grades(grades)        
    

    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValue) < 10 or (event.unicode == '.' and self.__pointsCount == 0):
                self.__strValue += event.unicode
                self.__grades = float(self.__strValue)
                if event.unicode == '.':
                    self.__pointsCount += 1
            elif event.key == K_BACKSPACE and self.__strValue != '':
                if self.__strValue[-1] == '.':
                    self.__pointsCount = 0
                self.__strValue = self.__strValue[:-1]
                self.grades(self.__strValue)

    def render(self):
        textBlock = self.__font.render(self.__strValue, True, (74, 74, 74))
        rect = textBlock.get_rect()
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size
        return {
            "bg": rect,
            "text": textBlock
        }

    def grades(self, grad=None):
        if grad is None:
            return self.__grades
        else: 
            grad = str(grad)
            try:
                self.__grades = float(grad)
                self.__strValue = grad
            except:
                pass

    def width(self, val=None):
        if val is None:
            return self.__size[0]
        else:             
            try:
                self.__size[0] = int(val)
            except:
                pass

    def height(self, val=None):
        if val is None:
            return self.__size[1]
        else:             
            try:
                self.__size[1] = int(val)
            except:
                pass
    
    def size(self, val=None):
        if val == None:
            return self.__size
        else:
            try:
                w = int(val[0])
                h = int(val[1])
                self.__size = [w, h]
            except:
                pass

    def posX(self, val=None):
        if val is None:
            return self.__position[0]
        else:             
            try:
                self.__position[0] = int(val)
            except:
                pass

    def posY(self, val=None):
        if val is None:
            return self.__position[1]
        else:             
            try:
                self.__position[1] = int(val)
            except:
                pass
    
    def pos(self, val=None):
        if val == None:
            return self.__position
        else:
            try:
                x = int(val[0])
                y = int(val[1])
                self.__position = [x, y]
            except:
                pass


class mainApp():
    thermometer = None
    entrada = None
    selector = None

    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Thermometer")        
        
        self.thermometer = Thermometer()        
        self.input = NumberInput()
        self.input.pos((106, 58))
        self.input.size((133, 28))

        self.selector = Selector()

    def __onClose(self):
        pygame.quit()
        sys.exit()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__onClose()
                
                self.input.on_event(event) 
                if event.type == MOUSEBUTTONDOWN:
                    self.selector.change() 
                    grades = self.input.grades()        
                    newUnit = self.selector.getUnit()           
                    temperature = self.thermometer.convert(grades, newUnit)
                    self.input.grades(temperature)
        
            # backgorund
            self.__screen.fill((244,236,203))
            # thermometer
            self.__screen.blit(self.thermometer.custome, (50, 34))
            # textbox
            text = self.input.render()
            pygame.draw.rect(self.__screen, (255, 255, 255), text["bg"])
            self.__screen.blit(text["text"], self.input.pos())
            # selector
            self.__screen.blit(self.selector.getCustome(), (112, 153))

            pygame.display.flip()

if __name__ == "__main__":
    pygame.font.init()
    app = mainApp()
    app.start()
