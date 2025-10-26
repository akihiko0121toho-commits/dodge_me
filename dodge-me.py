import pygame
pygame.init()

screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("My First Game")

runnning = True
while running:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			runnning = False
			
		screen.fill((255,255,255)) #白い背景
		pygame.display.flip()
		
	pygame.quit()

