import pygame
screen_size =[360,600]
screen=pygame.display.set_mode(screen_size)
background=pygame.image.load('nikhil.jpg')
screen.blit(background,[0,0])
keep_alive = True
while keep_alive:
	screen.blit(background,[0,0])
	pygame.display.update()
	planet=pygame.image.load('p_one.png')
	screen.blit(planet,[140,50])