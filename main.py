import pygame
from settings import *
from menu import *
from creator import *
from play import *
from player import Player

pygame.init()

# music
# crazy_frog = pygame.mixer.music.load('music\crazyfrog.mp3')
# pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(0.2)

playGame = False

screen = pygame.display.set_mode(size)
player = Player()

# menu buttons
creatorButton = Button(screen, 100, 300, 200, 100, image = None, font = font, writing = 'creator', wchx = 10, wchy = 10, writingColor = BLACK, color = GREY, strokeColor = BLACK, strokeWidth = 10)
playButton = Button(screen, 350, 300, 200, 100, image = None, font = font, writing = 'play', wchx = 10, wchy = 10, writingColor = BLACK, color = BEAUTIFULGREEN, strokeColor = BLACK, strokeWidth = 10)

# win menu
mainMenu = Button(screen, 250, 300, 250, 100, image = None, font = font, writing = 'main menu', wchx = 10, wchy = 10, writingColor = BLACK, color = BEAUTIFULGREEN, strokeColor = BLACK, strokeWidth = 10)

# creator buttons
clickType = ''

buttonWall = Button(screen, 10, 10, 50, 50, wallImage, color = GREY, strokeColor = BLACK, strokeWidth = 10)
buttonDelete = Button(screen, 380, 10, 50, 50, trashBinImage, color = GREY, strokeColor = BLACK, strokeWidth = 10)
buttonBall = Button(screen, 10, 80, 50, 50, ballImage, color = GREY, strokeColor = BLACK, strokeWidth = 10)
buttonNew = Button(screen, 85, 10, 50, 50, newImage, color = GREY, strokeColor = BLACK, strokeWidth = 10)
buttonSave = Button(screen, 305, 10, 50, 50, saveImage, color = GREY, strokeColor = BLACK, strokeWidth = 10)
buttonEmpty = Button(screen, 10, 220, 50, 50, emptyImage, color = GREY, strokeColor = BLACK, strokeWidth = 10)
buttonJumpingBall = Button(screen, 10, 150, 50, 50, jumpingBallImage, color = GREY, strokeColor = BLACK, strokeWidth = 10)
buttonChoiseLevel = Button(screen, 160, 10, 50, 50, choiceLevelImage, color = GREY, strokeColor = BLACK, strokeWidth = 10)
buttonClearAll = Button(screen, 235, 10, 50, 50, clearAllImage, color = GREY, strokeColor = BLACK, strokeWidth = 10)
buttonExit = Button(screen, 455, 10, 50, 50, font=font, writing='x', wchx = 10, writingColor=(0, 0, 0), image=None, color = BEAUTIFULRED, strokeColor = BLACK, strokeWidth = 10)


buttonCheckPoint = Button(screen, 10, 290, 50, 50, checkPointImage, color = GREY, strokeColor = BLACK, strokeWidth = 10)
buttonSpawnPoint = Button(screen, 10, 430, 50, 50, spawnPointImage, color = GREY, strokeColor = BLACK, strokeWidth = 10)
buttonEndPoint = Button(screen, 10, 360, 50, 50, endPointImage, color = GREY, strokeColor = BLACK, strokeWidth = 10)


clickTypeWriting = font.render('click type: ' + clickType, False, (0, 0, 0))

# selectorSpawn = Selector(screen, 100, 100, selectorMain, selectedNope, selectedS, selectedCh, selectedE)

scene = 'main'
pause = -1

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE and playGame:
				pause *= -1
#------------------=======================================PAUSE==========================================================-------------------------
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = pygame.mouse.get_pos()
		
			if event.button == 1:
				if scene == 'main':
					playGame = False
					player.moved_ever = False
					pause = -1
					scene = creatorButton.press(mouse_pos, 'creator', 'main', False)
					if scene != 'creator':
						scene = playButton.press(mouse_pos, 'play', 'main', False)
#------------------==========================================GAME==========================================-------------------------------------
				if scene == 'youWin':
					scene = mainMenu.press(mouse_pos, 'main', 'youWinw')
					

				if pause > 0:
					scene = exitTo.press(mouse_pos, 'main')
					pause = returnToGame.press(mouse_pos, -1, 1)
					if scene == 'main':
						playGame = False
						pause = -1

				if scene == 'play' and playGame != True:
					close = Button(screen, 580, 380, 50, 50, font=font, writing='x', wchx = 10, writingColor=(0, 0, 0), image=None, color = BEAUTIFULRED, strokeColor = BLACK, strokeWidth = 10)
					scene = close.press(mouse_pos, 'main', 'play', False)
					pygame.draw.rect(screen, BLACK, (50, 50, 600, 400), 10)
					pygame.draw.rect(screen, CYAN, (50, 50, 600, 400))

					levels = createButtonsOnLevels(screen, font)
					for i in levels:
						playingLevel = i.press(mouse_pos, i.justWriting)
						if playingLevel == i.justWriting:
							mas, editingLevel = readFile(i.justWriting)
							print (mas)
							playGame = True
							walls = getWalls(screen, mas, 50)
							balls = getBalls(mas)
							jumpingBalls = getJumpingBalls(mas)
							spawnPoint = getSpawnPoint(mas)
							endPoints = getEndPoints(mas)
							checkPoints = getCheckPoints(mas)
						i.draw()
					
					close.draw()
					

#------------------=========================================CREATOR========================================-------------------------------------					
				if scene == 'creator':

					# buttons
					clickType = buttonWall.press(mouse_pos, 'wall')

					if clickType != 'wall':
						clickType = buttonBall.press(mouse_pos, 'ball')

					if clickType != 'wall' and clickType != 'ball':
						clickType = buttonEmpty.press(mouse_pos, 'empty')
					
					if clickType != 'wall' and clickType != 'ball' and clickType != 'empty':
						clickType = buttonSpawnPoint.press(mouse_pos, 'spawnPoint')

					if clickType != 'wall' and clickType != 'ball' and clickType != 'empty' and clickType != 'spawnPoint':
						clickType = buttonCheckPoint.press(mouse_pos, 'checkPoint')

					if clickType != 'wall' and clickType != 'ball' and clickType != 'empty' and clickType != 'spawnPoint' and clickType != 'checkPoint':
						clickType = buttonEndPoint.press(mouse_pos, 'endPoint')

					if clickType != 'wall' and clickType != 'ball' and clickType != 'empty' and clickType != 'spawnPoint' and clickType != 'checkPoint' and clickType != 'endPoint':
						clickType = buttonJumpingBall.press(mouse_pos, 'jumpingBall')

					# selectorSpawn.change(mouse_pos)
					create = creteNew = buttonNew.press(mouse_pos, 'create')
					saveNew = buttonSave.press(mouse_pos, 'save')

					if create:
						createNewFile()

					if saveNew == 'save':
						try:
							saveChanges(mas, editingLevel)# str(mas))
						except NameError:
							print('no editing Level')
					clickTypeWriting = font.render('click type: ' + str(clickType), False, (0, 0, 0))
					
					scene = buttonChoiseLevel.press(mouse_pos, 'openToEdit', 'creator', False)
					
					if scene != 'openToEdit':
						scene = buttonDelete.press(mouse_pos, 'deleteLevel', 'creator', False)

					if scene != 'openToEdit' and scene != 'deleteLevel':
						scene = buttonExit.press(mouse_pos, 'main', 'creator', False) 
					mas = buttonClearAll.press(mouse_pos, [], mas)
				
				if scene == 'openToEdit':
					close = Button(screen, 580, 380, 50, 50, font=font, writing='x', wchx = 10, writingColor=(0, 0, 0), image=None, color = BEAUTIFULRED, strokeColor = BLACK, strokeWidth = 10)
					scene = close.press(mouse_pos, 'creator', 'openToEdit')
					pygame.draw.rect(screen, BLACK, (50, 50, 600, 400), 10)
					pygame.draw.rect(screen, CYAN, (50, 50, 600, 400))
					levels = createButtonsOnLevels(screen, font)

					for i in levels:
						opened = i.press(mouse_pos, 'open')
						if opened == 'open':
							mas, editingLevel = readFile(i.justWriting)
							print (editingLevel)
						i.draw()
					
					close.draw()

				if scene == 'deleteLevel':
					close = Button(screen, 580, 380, 50, 50, font=font, writing='x', wchx = 10, writingColor=BLACK, image=None, color = BEAUTIFULRED, strokeColor = BLACK, strokeWidth = 10) 
					scene = close.press(mouse_pos, 'creator', 'deleteLevel')
					levels = createButtonsOnLevels(screen, font)
					
					pygame.draw.rect(screen, BLACK, (50, 50, 600, 400), 10)
					pygame.draw.rect(screen, CYAN, (50, 50, 600, 400))
					close.draw()

					for i in levels:
						opened = i.press(mouse_pos, 'open')
						i.draw()
						if opened == 'open':
							deleteLevel(i.justWriting)
							print(i.justWriting + '.npy')
							print ('level Deleted')

					
					
			if event.button == 3:
				if mouse_pos[0] // 36 <= 16 and mouse_pos[0] // 36 >= 2:
					if mouse_pos[1] // 36 < 12 and mouse_pos[1] // 36 >= 2:
						if clickType == 'wall' and not findElem(mas, (mouse_pos[0]//36, mouse_pos[1]//36)):
							mas.append((mouse_pos[0]//36, mouse_pos[1]//36, 'wall'))

						if clickType == 'ball'and not findElem(mas, (mouse_pos[0]//36, mouse_pos[1]//36)):
							mas.append((mouse_pos[0]//36, mouse_pos[1]//36, 'ball'))

						if clickType == 'jumpingBall'and not findElem(mas, (mouse_pos[0]//36, mouse_pos[1]//36)):
							mas.append((mouse_pos[0]//36, mouse_pos[1]//36, 'jumpingBall'))

						if clickType == 'empty':
							deleteObj(mas, (mouse_pos[0]//36, mouse_pos[1]//36))

						if clickType == 'spawnPoint'and not findElem(mas, (mouse_pos[0]//36, mouse_pos[1]//36)):
							mas.append((mouse_pos[0]//36, mouse_pos[1]//36, 'spawnPoint'))

						if clickType == 'checkPoint'and not findElem(mas, (mouse_pos[0]//36, mouse_pos[1]//36)):
							mas.append((mouse_pos[0]//36, mouse_pos[1]//36, 'checkPoint'))

						if clickType == 'endPoint'and not findElem(mas, (mouse_pos[0]//36, mouse_pos[1]//36)):
							mas.append((mouse_pos[0]//36, mouse_pos[1]//36, 'endPoint'))
			# if event.button == 2:
			# 	openDir(screen, font2)

	keys = pygame.key.get_pressed()

	if scene == 'main':
		drawBackGround(screen, font2, font3)
		creatorButton.draw()
		playButton.draw()

	elif scene == 'creator':
		drawCreatorMenu(screen, 18, mas)
		buttonWall.draw()
		buttonBall.draw()
		buttonNew.draw()
		buttonSave.draw()
		buttonEmpty.draw()
		buttonSpawnPoint.draw()
		buttonCheckPoint.draw()
		buttonEndPoint.draw()
		buttonJumpingBall.draw()
		buttonChoiseLevel.draw()
		buttonDelete.draw()
		buttonClearAll.draw()
		buttonExit.draw()
		# selectorSpawn.draw()
		screen.blit(clickTypeWriting, (125, 435))

	if playGame:
		player. __reinit__(screen, walls, balls, endPoints, spawnPoint, checkPoints)
		player.move(keys)
		player.die(jumpingBalls)
		player.getCheckPoint()

		drawBg(screen, 50)

		if walls:
			for wall in walls:
				wall.draw()

		if spawnPoint:
			pygame.draw.rect(screen, (80, 225, 120), (spawnPoint[0] * 50, spawnPoint[1] * 50, 50, 50))

		if checkPoints:
			for point in checkPoints:
				pygame.draw.rect(screen, (80, 255, 120), (point[0] * 50, point[1] * 50, 50, 50))

		if endPoints:
			for point in endPoints:
				pygame.draw.rect(screen, (80, 255, 120), (point[0] * 50, point[1] * 50, 50, 50))

		if balls:
			for ball in balls:
				pygame.draw.circle(screen, (0, 122, 122), (ball[0] * 50 + 50//2, ball[1] * 50 + 50//2), 50//4)
		
		if jumpingBalls:
			for ball in jumpingBalls:
				ball.move(walls)
				ball.draw(screen)


		player.draw()
		if player.endGame():
			scene = 'youWin'
			playGame = False

			pygame.draw.rect(screen, BLACK, (50, 50, 600, 400), 10)
			pygame.draw.rect(screen, CYAN, (50, 50, 600, 400))
			win = font3.render('you win!!!', BLACK, False)
			screen.blit(win, (220, 80))

			mainMenu.draw()


	if pause == 1:
		pygame.draw.rect(screen, BLACK, (200, 50, 300, 400), 10)
		pygame.draw.rect(screen, CYAN, (200, 50, 300, 400))
		
		pauseWriting = font2.render('pause', BLACK, False)
		screen.blit(pauseWriting, (260, 50))

		exitTo = Button(screen, 250, 225, 200, 50, font=font, writing='menu', wchx = 30, writingColor=(0, 0, 0), image=None, color = GREY, strokeColor = BLACK, strokeWidth = 10)
		returnToGame = Button(screen, 250, 150, 200, 50, font=font, writing='return', wchx = 10, writingColor=(0, 0, 0), image=None, color = GREY, strokeColor = BLACK, strokeWidth = 10)

		exitTo.draw()
		returnToGame.draw()
	
	clock.tick(FPS)
	pygame.display.update()