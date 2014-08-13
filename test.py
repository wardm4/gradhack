import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400,400))

pygame.event.set_allowed(None)
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])


i=0
while True:
    e = pygame.event.wait()
    if e.type == 12:
    	pygame.quit()
        sys.exit()
    print e.key

    i += 1
