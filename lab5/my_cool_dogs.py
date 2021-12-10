import pygame
from pygame.draw import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SUN_BORDER = (255, 255, 128)
SUN_COLOR = (255, 255, 192)
SKY = (0, 255, 255)
WATER = (22, 80, 68)
GRAY = (32, 32, 32)


def draw_sun(x, y, r):
    line(screen, SUN_COLOR, (x - r, y), (x + r, y), r // 10)
    line(screen, SUN_COLOR, (x, y - r), (x, y + r), r // 10)
    circle(screen, SUN_BORDER, (x, y), r // 10, 0)
    circle(screen, SUN_BORDER, (x, y), r, r // 10)


def draw_hole(surface, x, y, r):
    s = (1 - r // abs(r)) // 2
    r0 = abs(r)

    ellipse(surface, GRAY, [x - (5 * r) // 2 + 5 * r * s, y - (3 * r0) // 4, 5 * r0, (11 * r0) // 8], 0)
    ellipse(surface, WATER, [x - 2 * r + 4 * r * s, y - r0 // 2, 4 * r0, r0], 0)


def draw_ear(surface, x, y, r):
    s = (1 - r // abs(r)) // 2
    r0 = abs(r)

    circle(surface, WHITE, (x, y), r0, 0)
    circle(surface, BLACK, (x, y), r0, 1)
    rect(surface, WHITE, [x - r // 2 + (3 * r * s) // 2, y, (3 * r0) // 2, r0], 0)


def draw_head(surface, x, y, r):
    s = (1 - r // abs(r)) // 2
    r0 = abs(r)

    ellipse(surface, WHITE, [x + 6 * r * s, y, 6 * r0, 3 * r0], 0)
    ellipse(surface, BLACK, [x + 6 * r * s, y, 6 * r0, 3 * r0], 1)

    # mouth
    ellipse(surface, BLACK, [x + 3 * r + (5 * r * s) // 2, y + 2 * r0, (5 * r0) // 2, (2 * r0) // 5], 1)
    rect(surface, WHITE, [x + 3 * r + (5 * r * s) // 2, y + 2 * r0, (5 * r0) // 2, r0 // 5], 0)

    # eyes
    circle(surface, BLACK, (x + 5 * r, y + r0), r0 // 5, 0)
    circle(surface, BLACK, (x + 3 * r + r // 2, y + r0), r0 // 5, 0)

    draw_ear(surface, x + r, y + (3 * r0) // 5, (3 * r) // 5)


def draw_bear(surface, x, y, r):
    # in case r is negative:
    s = (1 - r // abs(r)) // 2
    r0 = abs(r)

    draw_head(surface, x + 3 * r, y - 2 * r0, r)

    # body
    ellipse(surface, WHITE, [x + 8 * r * s, y, 8 * r0, 16 * r0], 0)
    ellipse(surface, BLACK, [x + 8 * r * s, y, 8 * r0, 16 * r0], 1)

    draw_hole(surface, x + 19 * r, y + 12 * r0, 2 * r)

    # fishing rod
    line(surface, BLACK, (x + 8 * r + r // 2, y + 7 * r0), (x + 18 * r + r // 2, y - 3 * r0), 5)
    line(surface, BLACK, (x + 18 * r, y - 3 * r0 + r0 // 2), (x + 18 * r, y + 12 * r0), 1)

    # hand
    ellipse(surface, WHITE, [x + 6 * r + 5 * r * s, y + 4 * r0, 5 * r0, 2 * r0], 0)
    ellipse(surface, BLACK, [x + 6 * r + 5 * r * s, y + 4 * r0, 5 * r0, 2 * r0], 1)

    # leg
    ellipse(surface, WHITE, [x + 4 * r + 6 * r * s, y + 12 * r0, 6 * r0, 4 * r0], 0)
    ellipse(surface, BLACK, [x + 4 * r + 6 * r * s, y + 12 * r0, 6 * r0, 4 * r0], 1)
    ellipse(surface, WHITE, [x + 8 * r + r // 2 + 3 * r * s, y + 14 * r0, 3 * r0, 2 * r0], 0)
    ellipse(surface, BLACK, [x + 8 * r + r // 2 + 3 * r * s, y + 14 * r0, 3 * r0, 2 * r0], 1)


pygame.init()

FPS = 30
screen = pygame.display.set_mode((700, 900))

# background
rect(screen, SKY, (0, 0, 700, 450))
rect(screen, WHITE, (0, 450, 700, 450))
line(screen, BLACK, (0, 450), (700, 450), 1)

draw_sun(500, 200, 190)

bear = screen.subsurface([0, 0, 700, 900])
positions = [[20, 450, 10], [100, 730, 15], [650, 550, -10]]
for pos in positions:
    draw_bear(bear, pos[0], pos[1], pos[2])

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