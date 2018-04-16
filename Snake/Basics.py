from random import randint

import pygame


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
        self.width = width
        self.height = height
        self.fps = fps
        self.frameCount = 0
        pygame.init()

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


class Text(object):
    def __init__(self, game: Game, size=None, font=None):
        if size is None:
            self.size = 20
        else:
            self.size = size
        if font is None:
            fontpath = pygame.font.get_default_font()
            self.font = pygame.font.match_font(fontpath)
        else:
            self.font = pygame.font.match_font(font)
        self.object = pygame.font.Font(self.font, self.size)
        self.surface = None
        self.game = game

    def writeText(self, text, position=None, antialias=True, color=(0, 255, 0)):
        if position is None:
            position = [0, 0]
        self.surface = self.object.render(text, antialias, color)
        self.game.screen.blit(self.surface, position)

    def render(self, text, antialias=True, color=(0, 255, 0)):
        self.surface = self.object.render(text, antialias, color)

    def draw(self, position=None):
        if position is None:
            position = [0, 0]
        self.game.screen.blit(self.surface, position)


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
            print(str(i.position) + str(player.position))
        index += 1
    return False


def isCollision(player: Player, cube: Cube):
    if [player.x, player.y] == cube.position:
        return True
