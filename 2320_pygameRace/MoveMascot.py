import pygame, sys
from pygame.locals import *

class Runner():
    __customes = ("sonic", "megaman", "frank", "dino")

    def __init__(self, x=0, y=0, custome="Sonic"):
        self.custome = pygame.image.load("./images/{}.gif".format(custome))
        self.position = [x,y]
        self.name = ""

class Game():
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("./images/background.gif")
        pygame.display.set_caption('Python Mascot Race')
    
        self.runner = Runner(320, 240)

    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.runner.position[1] -= 5
                    elif event.key == K_DOWN:
                        self.runner.position[1] += 5
                    elif event.key == K_RIGHT:
                        self.runner.position[0] += 5
                    elif event.key == K_LEFT:
                        self.runner.position[0] -= 5
                    else:
                        pass
            self.__screen.blit(self.__background, (0,0))
            self.__screen.blit(self.runner.custome, self.runner.position)
            pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    game = Game()    
    game.start()