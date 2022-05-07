import pygame
from player import Player

class Wall:
	def __init__(self, screen, x, y, unit):
		self.x = int(x) - 2
		self.y = int(y) - 2
		self.unit = unit
		self.screen = screen

		self.hitbox = pygame.Rect((int(x) - 2) * unit, (int(y) - 2) * unit, unit, unit)

	def draw(self):
		pygame.draw.rect(self.screen, (80, 80, 120), (self.x * self.unit, self.y * self.unit, self.unit, self.unit))

class jumpingBall:
	def __init__(self, x, y, delta_x=0, delta_y=1):
		self.x = x
		self.y = y

		self.delta_x = delta_x
		self.delta_y = delta_y

		self.hitbox = pygame.Rect(x * 50 + 12, y * 50 + 12, 25, 25)
	
	def move(self, walls):
		self.hitbox = pygame.Rect(self.x - 12, self.y - 12, 25, 25)
		for wall in walls:
			if self.hitbox.colliderect(wall.hitbox):
				self.delta_y *= -1
				self.delta_x *= -1
		self.x += self.delta_x
		self.y += self.delta_y

	def draw(self, screen):
		pygame.draw.circle(screen, (0, 122, 122), (self.x, self.y), 12)


def getWalls(screen, level, unit):
	walls = []
	for block in level:
		if block[2] == 'wall':
			walls.append(Wall(screen, block[0], block[1], unit))
	return walls

def getSpawnPoint(level):
	spawnPoint = []
	for block in level:
		if block[2] == 'spawnPoint':	
			spawnPoint = [int(block[0]) - 2, int(block[1]) - 2]
			return spawnPoint

def getEndPoints(level):
	endPoints = []
	for block in level:
		if block[2] == 'endPoint':	
			endPoints.append([int(block[0]) - 2, int(block[1]) - 2])
	return endPoints

def getCheckPoints(level):
	checkPoints = []
	for block in level:
		if block[2] == 'checkPoint':	
			checkPoints.append([int(block[0]) - 2, int(block[1]) - 2])
	return checkPoints

def drawBg(screen, unit):
	counter = 0
	for x in range(0, 700, unit):
		for y in range(0, 550, unit):
			if counter % 2 == 0:
				color = (255, 255, 255)
			else:
				color = (50, 50, 50)
			pygame.draw.rect(screen, color, (x, y, unit, unit))
			counter += 1
def getBalls(level):
	balls = []
	for block in level:
		if block[2] == 'ball':	
			balls.append([int(block[0]) - 2, int(block[1]) - 2])
	return balls

def getJumpingBalls(level):
	jumpingBalls = []
	for block in level:
		if block[2] == 'jumpingBall':	
			jumpingBalls.append(jumpingBall((int(block[0]) - 2) * 50 + 25, (int(block[1]) - 2) * 50 + 25, delta_y=2))
	return jumpingBalls

# def play(screen, level, unit, player, walls, balls, endPoints, spawnPoint, checkPoints, clock):
# 	clock.tick(60)
# 	# screen.fill((0, 122, 122))
# 	drawBg(screen, unit)

# 	if walls:
# 		for wall in walls:
# 			wall.draw()

# 	if spawnPoint:
# 		pygame.draw.rect(screen, (80, 225, 120), (spawnPoint[0] * unit, spawnPoint[1] * unit, unit, unit))

# 	if checkPoints:
# 		for point in checkPoints:
# 			pygame.draw.rect(screen, (80, 255, 120), (point[0] * unit, point[1] * unit, unit, unit))

# 	if endPoints:
# 		for point in endPoints:
# 			pygame.draw.rect(screen, (80, 255, 120), (point[0] * unit, point[1] * unit, unit, unit))

# 	if balls:
# 		for ball in balls:
# 			pygame.draw.circle(screen, (0, 122, 122), (ball[0] * unit + unit//2, ball[1] * unit + unit//2), unit//4)

# 	player.draw()