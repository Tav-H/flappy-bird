import pygame
import random
pygame.init()
pygame.display.set_caption('flappy bird')
def end_game():
	print('your final score was: ' + str(score-1))
	pygame.quit()
	exit()
	exit()
sizex = 300
sizey = 400
window = pygame.display.set_mode((sizex, sizey))
clock = pygame.time.Clock()
rect = pygame.Rect(0, 0, 20, 20)
rect.center = window.get_rect().center
vel = 2
x = 10
y = sizey/2
freeze = False
up = False
start = False
run = True
peak = 0
jumpheight = 7
pipeheight = int(sizey*2 - 160)
pipewidth = int((pipeheight/1080) * 76)
backgroundlength = int((sizey/496) * 379)
body = pygame.transform.scale(pygame.image.load('bird.png'), (50, 50))
background = pygame.transform.scale(pygame.image.load('flappy bird background2.png'), (backgroundlength, sizey))
pipe = pygame.transform.scale(pygame.image.load('pipe.png'), (pipewidth, pipeheight))
bodyup = pygame.transform.rotate(body,10)
bodydown = pygame.transform.rotate(body,-10)
check = False
backgroundplace = sizex
pipeplace1 = sizex
score = 0
pipeplace2 = sizex + sizex-40
check = False
pipeheight1 = random.randint(-242, 0)
pipeheight2 = random.randint(-242, 0)
pipeheightnow = pipeheight1
while run:
	clock.tick(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		mouse_presses = pygame.mouse.get_pressed()
		if mouse_presses[0]:
			run = False
		if event.type == pygame.KEYDOWN:
			if pygame.key.name(event.key) == 'space':
				run = False
	window.blit(background, (0, 0))
	window.blit(bodyup, (10, 11))
	pygame.display.flip()
run = True
boost = False
while run:
	pipeplace1 -= 2
	pipeplace2 -= 2
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		mouse_presses = pygame.mouse.get_pressed()
		if mouse_presses[0]:
			x = -1
			peak = y - jumpheight**2
		if event.type == pygame.KEYDOWN:
			if pygame.key.name(event.key) == 'space':
				x = -1
				peak = y - jumpheight**2
			if pygame.key.name(event.key) == 'b':
				boost = True
		if event.type == pygame.KEYUP:
			if pygame.key.name(event.key) == 'b':
				boost = False
	prevy = y
	if not freeze:
		x += 1
	if up:
		start = True
		up = False
	if not boost:
		y = (((1/3)*x-jumpheight)**2) + peak
	else:
		y = ((x-jumpheight)**2) + peak
	if prevy > y:
		if y < -10 and x > 1:
			window.blit(bodyup, (10, -1))
			freeze = False
			x = 25
			peak = 0
		else:
			window.blit(bodyup, (10, y))
			freeze = False
	else:
		if x > 1 and y > sizey-50:
			freeze = True
			window.blit(bodydown, (10, sizey-50))
		else:
			freeze = False
			window.blit(bodydown, (10, y))


	if pipeplace1 == 40:
		pipeplace2 = sizex
		pipeheight2 = random.randint(-242, 0)
		pipeheightnow = pipeheight1
		check = True
		score += 1
	if pipeplace2 == 40:
		pipeplace1 = sizex
		pipeheight1 = random.randint(-242, 0)
		pipeheightnow = pipeheight2
		check = True
		score += 1
	if pipeplace1 == -4 or pipeplace2 == -4:
		check = False

	if check:
		if y + 19 < 275 + pipeheightnow:
			end_game()
			
		elif y + 41 > 367 + pipeheightnow:
			end_game()
			
	#pygame.draw.rect(window, (255, 255, 255), pygame.Rect(40, (y+19), 10, 22))
	#pygame.draw.rect(window, (0, 0, 0), pygame.Rect(40, 275 + pipeheightnow, 10, 22))
	#pygame.draw.rect(window, (0, 0, 0), pygame.Rect(40, 367 + pipeheightnow, 10, 22))
	pygame.display.flip()
	window.blit(background, (0, 0))
	window.blit(pipe, (pipeplace1, pipeheight1))
	window.blit(pipe, (pipeplace2, pipeheight2))
end_game()





