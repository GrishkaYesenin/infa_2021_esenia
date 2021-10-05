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

# sun
x, y, r = (500, 200, 190)

line(screen, SUN_COLOR, (x - r, y), (x + r, y), r // 10)
line(screen, SUN_COLOR, (x, y - r), (x, y + r), r // 10)
circle(screen, SUN_BORDER, (x, y), r // 10, 0)
circle(screen, SUN_BORDER, (x, y), r, r // 10)

# hole
surface = screen.subsurface([0, 0, 700, 900])
hole_position = (200, 730, 30)

x, y, r = hole_position
s = (1 - r // abs(r)) // 2
r0 = abs(r)

ellipse(surface, GRAY, [x - (5 * r) // 2 + 5 * r * s, y - (3 * r0) // 4, 5 * r0, (11 * r0) // 8], 0)
ellipse(surface, WATER, [x - 2 * r + 4 * r * s, y - r0 // 2, 4 * r0, r0], 0)


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