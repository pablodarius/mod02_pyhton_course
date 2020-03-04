import pygame 

class Game():
    runners = []

    def __init__(self):
        self.__screen = pygame.display.set_mode([640,480])
        pygame.display.set_caption('Mascot Race Python')
        self.background = pygame.image.load("./images/background.gif")
        self.runner = pygame.image.load("./images/sonic.gif")

    def startRace(self):
        x = 0
        winner = False

        while not winner:
            # events listener
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            # refresh and render display
            self.__screen.blit(self.background, (0,0))
            self.__screen.blit(self.runner, (x, 240))
            pygame.display.flip()

            x += 0.25
            if x >= 600:
                winner = True
        
        pygame.quit()
        exit()

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.startRace()