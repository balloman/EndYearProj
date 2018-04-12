import pygame

pygame.init()
height = 300
width = 400
screen = pygame.display.set_mode((width, height))
done = False
is_blue = True
cor_height = height - 20
cor_width = width - 20
x = 0
y = cor_height
speed = 20
clock = pygame.time.Clock()
direction = [0, 0]
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

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

    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    screen.fill((0, 0, 0))

    if 0 >= x and direction[0] == -speed:
        x += 0
    elif x >= cor_width and direction[0] == speed:
        x += 0
    else:
        x += direction[0]
    if 0 >= y and direction[1] == -speed:
        y += 0
    elif y >= cor_height and direction[1] == speed:
        y += 0
    else:
        y += direction[1]
    print("Values: " + str(x) + ", " + str(y))

    pygame.draw.rect(screen, color, pygame.Rect(x, y, 20, 20))
    pygame.display.flip()
    clock.tick(5)
