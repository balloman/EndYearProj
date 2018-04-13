import pygame
from random import randint

HEIGHT = 1080
WIDTH = 1920


def control(speed):
    direction = [0,0]
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        direction[1] = -speed
        direction[0] = 0
    if pressed[pygame.K_DOWN]:
        direction[1] = speed
        direction[0] = 0
    if pressed[pygame.K_LEFT]:
        direction[0] = -speed
        direction[1] = 0
    if pressed[pygame.K_RIGHT]:
        direction[0] = speed
        direction[1] = 0
    return direction

class Game(object):
    clock = pygame.time.Clock()

    def __init__(self, width, height, mode, fps=60):
        self.screen = pygame.display.set_mode((width, height), mode)
        self.cor_width = width - 60
        self.cor_height = height - 60
        self.fps = fps

    def setFPS(self, i_fps):
        self.fps = i_fps

    def setDisplay(self, width, height, mode):
        self.screen = pygame.display.set_mode((width, height), mode)


class Player(object):

    def __init__(self, screen, rect, color=(0, 0, 255)):
        self.screen = screen
        self.color = color
        self.rect = rect
        self.direction = [0,0]

    def



def start():
    game = Game(WIDTH, HEIGHT, pygame.FULLSCREEN)
    game.setFPS(10)
    while True:
        game.clock.tick()
