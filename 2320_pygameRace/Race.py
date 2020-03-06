import pygame, sys
import random

class Runner():
    def __init__(self, x=0, y=0):
        self.custom = pygame.image.load("./images/sonic.gif")
        self.position = [x,y]
        self.name = "Sonic"
    
    def run(self):
        self.position[0] += random.randint(1,12)

class Game():
    runners = []
    __startLine = 5
    __finishLine = 620    

    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("./images/background.gif")
        pygame.display.set_caption('Python Mascot Race')
        self.runners.append(Runner(self.__startLine, 240))

    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                
                self.runners[0].run()

                if self.runners[0].position[0] >= self.__finishLine:
                    print("And the winner is {}".format(self.runners[0].name))
                    gameOver = True

                self.__screen.blit(self.__background, (0,0))
                self.__screen.blit(self.runners[0].custom, self.runners[0].position)
                pygame.display.flip()
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    pygame.init()
    game.start()