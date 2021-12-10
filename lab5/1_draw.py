import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 175), 150)
circle(screen, (255, 0, 0), (250, 150), 30)
circle(screen, (255, 0, 0), (150, 150), 30)
rect(screen, (10, 80, 0), (150, 250, 70, 10))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
