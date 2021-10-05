import pygame
from pygame.draw import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SUN_BORDER = (255, 255, 128)
SUN_COLOR = (255, 255, 192)
SKY = (0, 255, 255)
WATER = (22, 80, 68)
GRAY = (32, 32, 32)


pygame.init()

FPS = 30
screen = pygame.display.set_mode((700, 900))

# background
rect(screen, SKY, (0, 0, 700, 450))
rect(screen, WHITE, (0, 450, 700, 450))
line(screen, BLACK, (0, 450), (700, 450), 1)

x, y, r = (500, 200, 190)

line(screen, SUN_COLOR, (x - r, y), (x + r, y), r // 10)
line(screen, SUN_COLOR, (x, y - r), (x, y + r), r // 10)
circle(screen, SUN_BORDER, (x, y), r // 10, 0)
circle(screen, SUN_BORDER, (x, y), r, r // 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    pygame.display.update()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (pygame.time.get_ticks() > 5000):
            finished = True

pygame.quit()