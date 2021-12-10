import math
from random import choice

import pygame
import sys
import random as rnd

pygame.font.init()
FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

GUN_POS = (40, 450)

pygame.display.set_caption("Попади если сможешь")

pygame.font.init()
f1 = pygame.font.SysFont('serif', 36)

class Ball:
    def __init__(self, screen: pygame.Surface, x=GUN_POS[0], y=GUN_POS[1]):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.life_time = 100

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        self.x += self.vx
        self.y += self.vy

        self.vy += 1

        if self.y + self.r >= HEIGHT -5 or self.y <= self.r:
            self.vy *= -0.5
            self.vx *= 0.5

        if self.x + self.r>= WIDTH or self.x <= self.r:
            self.vx *= -0.5
            self.vy *= 0.5

        if abs(self.vy) <= 0.5:
            self.vy = 0

        self.life_time -= 1

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        s = ((self.y-obj.y)**2 + (self.x-obj.x)**2)**(0.5)
        if s <= self.r + obj.r:
            return True
        else:
            return False




class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.angle = 1
        self.color = GREY
        self.start_pos = GUN_POS
        self.width = 10
        self.len = 20

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.angle = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.angle)
        new_ball.vy = self.f2_power * math.sin(self.angle)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        self.len = 20

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.angle = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        # FIXIT don't know how to do it
        end_pos = self.start_pos[0] + self.len*math.cos(self.angle), self.start_pos[1] + self.len*math.sin(self.angle)
        pygame.draw.line(
            self.screen,
            self.color,
            self.start_pos,
            end_pos,
            self.width
        )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100 and self.len < 100:
                self.f2_power += 1
                self.len += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, screen):
        self.screen = screen
        self.points = 0
        self.new_target()

    # FIXME: don't work!!! How to call this functions when object is created?

    def new_target(self):
        """ Инициализация новой цели. """
        self.live = 1
        x = self.x = rnd.uniform(600, 780)
        y = self.y = rnd.uniform(300, 550)
        vx = self.vx = rnd.uniform(-10, 10)
        vy = self.vy = rnd.uniform(-10, 10)
        r = self.r = rnd.uniform(2, 50)
        color = self.color = RED

    def hit(self, points=1):
        """Попадание шарика в цель."""
        global bullet
        self.points += points
        self.live = 0
        pygame.display.update()
        bullet = 0

    def draw(self):

        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def move(self):
        self.x += self.vx
        self.y += self.vy

        self.vy += 1

        if self.y + self.r >= HEIGHT - 5 or self.y <= self.r:
            self.vy *= -1

        if self.x + self.r >= WIDTH or self.x <= self.r:
            self.vx *= -1

        if abs(self.vy) <= 0.5:
            self.vy = 0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
targets = [Target(screen), Target(screen)]
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    for target in targets:
     target.draw()
    for b in balls:
        if b.life_time <= 0:
            balls.remove(b)
        else:
            b.draw()

    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        for target in targets:
            target.move()
            if b.hittest(target):
                target.life_time = 0
                target.hit()
                targets.remove(target)

        if not targets:
            targets =[Target(screen), Target(screen)]
            text = f1.render(f'Вы попали в обе цели за  выстрелов', True, (180, 0, 0))
            screen.blit(text, (10, 50))
    gun.power_up()

pygame.quit()