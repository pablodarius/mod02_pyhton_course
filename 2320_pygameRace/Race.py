import pygame, sys
import random

class Runner():
    __customes = ("sonic", "megaman", "frank", "dino")

    def __init__(self, x=0, y=0, custome=None):
        self.custome = pygame.image.load("./images/{}.gif".format(custome))
        self.position = [x,y]
        self.name = ""
    
    def run(self):
        self.position[0] += random.randint(1,12)

class Game():
    __runners = []
    __posY = (100, 200, 300, 400)
    __names = ("sonic", "megaman", "frank", "dino")
    __startLine = 5
    __finishLine = 620    

    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("./images/background.gif")
        pygame.display.set_caption('Python Mascot Race')

        for i in range(4):
            self.__runners.append(Runner(self.__startLine, self.__posY[i], self.__names[i]))
            self.__runners[i].name = self.__names[i]

    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                
                for item in self.__runners:
                    item.run()
                    if item.position[0] >= self.__finishLine:
                        print("And the winner is {}".format(item.name))
                        gameOver = True

                self.__screen.blit(self.__background, (0,0))
                for  item in self.__runners:
                    self.__screen.blit(item.custome, item.position)
                    pygame.display.flip()
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    pygame.font.init()
    game = Game()    
    game.start()