"""This is a much neater and more modular version of test.py with classes"""
import pygame

import Snake.Basics as base

HEIGHT = int(1080 / 2)
WIDTH = int(1920 / 2)


def start():
    """This is the class that actually runs the game lol"""
    game = base.Game(WIDTH, HEIGHT)
    game.setFPS(8)
    player1 = base.Player(game, [60, 60])
    text = base.Text(game, 50)
    game.screen.fill((0, 0, 0))
    done = False
    isFood = False
    places = []
    food = None
    while not done:
        done = base.quitCheck(player1)
        player1.move()
        player1.drawCube()
        for i in player1.tails:
            i.follow(places[game.frameCount - i.index])
        if isFood:
            if base.isCollision(player1, food):
                player1.eat()
                isFood = False
            else:
                food.drawCube()
        else:
            food = base.Cube(game)
            isFood = True
        text.writeText(("Score: " + str(player1.eaten)))
        places.append(player1.position)
        pygame.display.flip()
        game.screen.fill((0, 0, 0))
        game.tick()
    pygame.quit()


start()
