import pygame

pygame.init()
screen = pygame.display.set_mode((400,400))

pygame.event.set_allowed(None)
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])

while True:
    e = pygame.event.wait()
    print e