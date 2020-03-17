import pygame, sys
from pygame.locals import *

class Thermometer():
    def __init__(self):
        self.custome = pygame.image.load("./images/thermometer.png")

class NumberInput():
    __grades = 0
    __strValue = "0"
    __position = [0, 0]
    __size = [0, 0]

    def __init__(self, grades=0):
        self.__font = pygame.font.SysFont("Arial", 24)
        self.grades(grades)        
    

    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode in '01234567890' and len(self.__strValue) < 10:     # event.unicode.isdigit()  
                self.__strValue += event.unicode
            elif event.key == K_BACKSPACE:
                self.__strValue = self.__strValue[:-1]

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
                self.__grades = int(grad)
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
        self.__screen.fill((244,236,203))
        
        self.thermometer = Thermometer()        
        self.input = NumberInput()
        self.input.pos((106, 58))
        self.input.size((133, 28))


    def __onClose(self):
        pygame.quit()
        sys.exit()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__onClose()
                
                self.input.on_event(event)
                        
        
            self.__screen.blit(self.thermometer.custome, (50, 34))
            text = self.input.render()
            pygame.draw.rect(self.__screen, (255, 255, 255), text["bg"])
            self.__screen.blit(text["text"], self.input.pos())

            pygame.display.flip()

if __name__ == "__main__":
    pygame.font.init()
    app = mainApp()
    app.start()
