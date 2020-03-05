# import and initialize the pygame library
import pygame, sys
pygame.init()


width = 640
height = 480
screen = pygame.display.set_mode((width,height))
screen.fill((246,147,48))
background = pygame.image.load("./images/pygame_cycle.JPG")
pygame.display.set_caption("Basic Pygame Cycle")

gameOver = False
while not gameOver:
    # events listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        # refresh and render display
        screen.blit(background,(0,0))        
        pygame.display.flip()        

pygame.quit()
sys.exit()
