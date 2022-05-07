import pygame

def drawBackGround(screen, font, font2):
	screen.fill((0, 122, 122))
	# font = pygame.font.SysFont('fonts/INVASION2000.TTF', 20)
	mainText = font.render('World hardest game', False, (122, 122, 122))
	mainTextStroke = font2.render('World hardest game', False, (0, 0, 0))
	screen.blit(mainTextStroke, (55, 55))
	screen.blit(mainText, (50, 50))
	

class Button:
	def __init__(self, screen, x, y, w, h, image = None, font=None, writing=None, wchx=0, wchy=0, writingColor=None, color=(255, 255, 255), strokeColor=None, strokeWidth=10):
		self.screen = screen

		self.font = font
		if font:
			self.writing = font.render(writing, True, writingColor)
			
		self.justWriting = writing
		self.x = x
		self.y = y
		self.shx = x + 5
		self.shy = y + 5
		self.w = w
		self.h = h
		self.color = color
		self.strokeColor = strokeColor
		self.strokeWidth = strokeWidth

		self.hitbox = pygame.Rect(self.x, self.y, self.w, self.h)

		self.pressed = False

		self.frame = 0
		self.animate=True

		self.image = image

		self.wchx = wchx
		self.wchy = wchy
	
	def draw(self):
		if self.strokeColor:
			pygame.draw.rect(self.screen, self.strokeColor, (self.x, self.y, self.w, self.h), self.strokeWidth)
			pygame.draw.rect(self.screen, (0, 0, 0), (self.shx, self.shy, self.w, self.h), self.strokeWidth)

		pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))
		if self.font:
			self.screen.blit(self.writing, (self.x + self.wchx, self.y + self.wchy))
		if self.image:
			self.screen.blit(self.image, (self.x, self.y))
			
		if self.pressed:
			if self.animate:
				self.pressAnim(10)
			else:
				self.pressed = False
		
		# else: 
		# 	self.x -= 5
		# 	self.y -= 5

	def press(self, mouse_pos, ifTrue, ifFalse='', animate=True):
		self.animate = animate
		mouse = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
		if mouse.colliderect(self.hitbox):
			self.pressed = True
			return ifTrue
		else:
			return ifFalse

	def pressAnim(self, frames):
		self.frame += 1
		if self.frame <= frames // 2:
			self.x += 5 / (frames / 2)
			self.y += 5 / (frames / 2)

		if self.frame > frames // 2:
			self.x -= 5 / (frames / 2)
			self.y -= 5 / (frames / 2)

		if self.frame == frames:
			self.frame = 0

			self.pressed = False


