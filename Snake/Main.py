"""This is a much neater and more modular version of test.py with classes"""

from random import randint

import pygame

HEIGHT = 1080
WIDTH = 1920


def control(speed, direction=[0, 0]):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if direction[1] != speed:
            direction[1] = -speed
            direction[0] = 0
    if pressed[pygame.K_DOWN]:
        if direction[1] != -speed:
            direction[1] = speed
            direction[0] = 0
    if pressed[pygame.K_LEFT]:
        if direction[0] != speed:
            direction[0] = -speed
            direction[1] = 0
    if pressed[pygame.K_RIGHT]:
        if direction[0] != -speed:
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
        self.frameCount = 0

    def setFPS(self, i_fps):
        self.fps = i_fps

    def setDisplay(self, width, height, mode):
        self.screen = pygame.display.set_mode((width, height), mode)

    def tick(self):
        self.frameCount += 1
        self.clock.tick(self.fps)


class Cube(object):
    def __init__(self, game: Game, color=(255, 0, 0), position=None):
        self.game = game
        self.surface = game.screen
        self.color = color
        randNumbers = [randint(0, game.cor_width / 60) * 60, randint(0, game.cor_height / 60) * 60]
        if position is None:
            position = randNumbers
        self.position = position
        self.rect = pygame.Rect(position[0], position[1], 60, 60)

    def drawCube(self):
        pygame.draw.rect(self.surface, self.color, self.rect)


class Player(Cube):
    def __init__(self, game: Game, size: list, speed=60):
        self.x = 0
        self.y = game.cor_height
        self.position = [self.x, self.y]
        self.color = (0, 0, 255)
        super().__init__(game, color=self.color, position=self.position)
        self.size = size
        self.speed = speed
        self.eaten = 0
        self.tails = []

    def move(self):
        direction = control(60)
        self.x += direction[0]
        self.y += direction[1]
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.position = [self.x, self.y]

    def eat(self):
        self.eaten += 1
        self.tails.append(Tail(self.game, self.eaten))


class Tail(Cube):
    def __init__(self, game: Game, index: int):
        super().__init__(game, color=(0, 0, 255))
        self.index = index

    def follow(self, position):
        self.rect = pygame.Rect(position[0], position[1], 60, 60)
        self.drawCube()


def quitCheck(player: Player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            return True
        else:
            return False
    if player.x > player.game.cor_width or player.x < 0:
        return True
    if player.y > player.game.cor_height or player.y < 0:
        return True
    index = 0
    for i in player.tails:
        if index != 0 and player.position == i.position:
            return True
        index += 1
    return False


def isCollision(player: Player, cube: Cube):
    if [player.x, player.y] == cube.position:
        return True


def start():
    """This is the class that actually runs the game lol"""
    game = Game(WIDTH, HEIGHT, pygame.FULLSCREEN)
    game.setFPS(10)
    player1 = Player(game, [60, 60])
    game.screen.fill((0, 0, 0))
    done = False
    isFood = False
    places = []
    food = None
    while not done:
        done = quitCheck(player1)
        player1.move()
        player1.drawCube()
        for i in player1.tails:
            i.follow(places[game.frameCount - i.index])
        if isFood:
            if isCollision(player1, food):
                player1.eat()
                isFood = False
            else:
                food.drawCube()
        else:
            food = Cube(game)
            isFood = True

        places.append(player1.position)
        pygame.display.flip()
        game.screen.fill((0, 0, 0))
        game.tick()


start()
