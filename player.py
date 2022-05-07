import pygame

class Player:
	def __init__(self):
		self.moved_ever = False
		self.checkpoints = 0

	def __reinit__(self, screen, walls, balls, endPoints, spawnPoint, checkPoints):
		if not self.moved_ever:
			self.x, self.y = spawnPoint[0], spawnPoint[1]
		self.w = 25

		self.screen = screen

		self.walls = walls
		self.balls = balls
		
		self.endPoints = endPoints
		self.checkPoints = checkPoints
		self.hitbox = pygame.Rect(self.x * 50, self.y * 50, self.w, self.w)
		
		self.spawnPoint = spawnPoint
		
		if self.checkpoints == 0:
			self.respawnPoint = spawnPoint

	def draw(self):
		pygame.draw.rect(self.screen, (122, 122, 0), (self.x * 50, self.y * 50, self.w, self.w), 10)
		pygame.draw.rect(self.screen, (255, 255, 0), (self.x * 50, self.y * 50, self.w, self.w))

	def move(self, keys):
		self.moved_ever = True

		if keys[pygame.K_a] and self.nextPos(delta_x=-0.05):
			self.x -= 0.05
			self.hitbox = pygame.Rect(self.x * 50, self.y * 50, self.w, self.w)

		if keys[pygame.K_d] and self.nextPos(delta_x=0.05):
			self.x += 0.05
			self.hitbox = pygame.Rect(self.x * 50, self.y * 50, self.w, self.w)

		if keys[pygame.K_s] and self.nextPos(delta_y=0.05):
			self.y += 0.05
			self.hitbox = pygame.Rect(self.x * 50, self.y * 50, self.w, self.w)

		if keys[pygame.K_w] and self.nextPos(delta_y=-0.05):
			self.y -= 0.05
			self.hitbox = pygame.Rect(self.x * 50, self.y * 50, self.w, self.w)

	def die(self, jumpingBalls):
		for ball in self.balls:
			ballRect = pygame.Rect(ball[0] * 50 + 12, ball[1] * 50 + 12, 25, 25)
			if self.hitbox.colliderect(ballRect):
				self.x, self.y = self.respawnPoint[0], self.respawnPoint[1]
		for jBall in jumpingBalls:
			if self.hitbox.colliderect(jBall.hitbox):
				self.x, self.y = self.respawnPoint[0], self.respawnPoint[1]

	def getCheckPoint(self):
		for checkPoint in self.checkPoints:
			# print(checkPoint)
			checkPointRect = pygame.Rect(checkPoint[0] * 50, checkPoint[1] * 50, 50, 50)
			if self.hitbox.colliderect(checkPointRect):
				self.respawnPoint = checkPoint
				self.checkpoints = 1

		spawnPointRect = pygame.Rect(self.spawnPoint[0] * 50, self.spawnPoint[1] * 50, 50, 50)
		if self.hitbox.colliderect(spawnPointRect):
			self.respawnPoint = self.spawnPoint

	def endGame(self):
		for endPoint in self.endPoints:
			# print(endPoint)
			endPointRect = pygame.Rect(endPoint[0] * 50, endPoint[1] * 50, 50, 50)
			if self.hitbox.colliderect(endPointRect):
				return True

	def nextPos(self, delta_x=0, delta_y=0):
		nextPos = pygame.Rect((self.x + delta_x) * 50, (self.y + delta_y) * 50, 25, 25)
		for wall in self.walls:
			if nextPos.colliderect(wall.hitbox):
				return False
		return True
