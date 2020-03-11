import pygame, sys
from pygame.locals import *

class mainApp():
    thermometer = None
    entrada = None
    selector = None

    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Thermometer")
        self.__screen.fill((244,236,203))

    def __onClose(self):
        pygame.quit()
        sys.exit()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__onClose()
        
            pygame.display.flip()

if __name__ == "__main__":
    pygame.font.init()
    app = mainApp()
    app.start()

