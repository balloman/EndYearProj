"""This is a much neater and more modular version of test.py with classes"""

import pygame
from random import randint

HEIGHT = 540
WIDTH = 960


def control(speed, direction=[0, 0]):
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

    def __init__(self, width, height, mode=None, fps=60):
        if mode is None:
            self.screen = pygame.display.set_mode((width, height))
        else:
            self.screen = pygame.display.set_mode((width, height), mode)
        self.cor_width = width - 60
        self.cor_height = height - 60
        self.fps = fps

    def setFPS(self, i_fps):
        self.fps = i_fps

    def setDisplay(self, width, height, mode):
        self.screen = pygame.display.set_mode((width, height), mode)

    def tick(self):
        self.clock.tick(self.fps)


class Cube(object):
    def __init__(self, game: Game, color=(255, 0, 0), position=None):
        self.game = game
        self.surface = game.screen
        self.color = color
        if position is None:
            position = [randint(0, game.cor_width / 60) * 60, randint(0, game.cor_height / 60) * 60]
        self.position = position
        self.rect = pygame.Rect(position[0], position[1], 60, 60)

    def drawCube(self):
        pygame.draw.rect(self.surface, self.color, self.rect)


class Player(Cube):
    def __init__(self, game: Game, size: tuple, speed=60):
        self.x = 0
        self.y = game.cor_height
        self.position = [self.x, self.y]
        self.color = (0, 0, 255)
        super().__init__(game, self.color, self.position)
        self.size = size
        self.speed = speed

    def move(self):
        direction = control(60)
        if self.x <= 0 and direction[0] == -self.speed:
            self.x += 0
        else:
            self.x += direction[0]
        if self.y <= 0 and direction[1] == -self.speed:
            self.y += 0
        else:
            self.y += direction[1]
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def eat(self):
        pass


def quitCheck(player: Player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            return True
        else:
            return False
    if player.x > player.game.cor_width:
        return True
    if player.y > player.game.cor_height:
        return True
    return False


def start():
    """This is the class that actually runs the game lol"""
    game = Game(WIDTH, HEIGHT)
    game.setFPS(10)
    player1 = Player(game, (60, 60))
    game.screen.fill((0, 0, 0))
    done = False
    food = Cube(game)
    while not done:
        done = quitCheck(player1)
        player1.move()
        player1.drawCube()
        food.drawCube()
        pygame.display.flip()
        game.screen.fill((0, 0, 0))
        game.tick()


start()
