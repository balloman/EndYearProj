import pygame

pygame.init()
height = 400
width = 300
screen = pygame.display.set_mode((height, width))
done = False
is_blue = True
cor_height = height - 60
cor_width = width - 60
x=0
y=cor_width
clock = pygame.time.Clock()
direction = (0,0)
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			done = True
		if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			is_blue = not is_blue

	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP] and y >= 0:
		direction[1] = -4
	if pressed[pygame.K_DOWN] and y <= cor_width:
		direction[0] = 4
	if pressed[pygame.K_LEFT] and x >= 0:
		x = -3
	if pressed[pygame.K_RIGHT] and x <= cor_height:
		x = 3
	direction = (x, y)
	if is_blue:
		color = (0, 128, 255)
	else:
		color = (255, 100, 0)
	screen.fill((0, 0, 0))


	pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
	pygame.display.flip()
	clock.tick(60)
