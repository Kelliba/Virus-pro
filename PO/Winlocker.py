import pygame

pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Test Game")

x = 50 
y = 50
rad = 10
width = 40
height = 40
speed = 5

run = True
while run:
	pygame.draw.rect(win,(0,0,255),(x,y,width,height))
	pygame.time.delay(100)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT]:
		x -= speed
	if key[pygame.K_RIGHT]:
		x += speed

	
#Для покупки ПО свяжитесь с автором по почте.