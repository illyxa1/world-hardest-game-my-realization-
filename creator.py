import pygame
import os
from menu import Button

import numpy as np
counts = 0
def drawCreatorMenu(screen, unit, mas):
	counter = 0
	for x in range(72, 700, unit):
		for y in range(72, 514, unit):
			if counter % 2 == 0:
				color = (255, 255, 255)
			else:
				color = (50, 50, 50)
			pygame.draw.rect(screen, color, (x, y, unit, unit))
			counter += 1
	pygame.draw.rect(screen, (122, 122, 122), (0, 0, 700, 72))
	pygame.draw.rect(screen, (122, 122, 122), (0, 0, 72, 500))
	pygame.draw.rect(screen, (122, 122, 122), (612, 0, 90, 500))
	pygame.draw.rect(screen, (122, 122, 122), (0, 432, 700, 69))
	if mas:
		for i in mas:
			if i[2] == 'wall':
				pygame.draw.rect(screen, (80, 80, 120), (int(i[0]) * 36, int(i[1]) * 36, 36, 36)) # (255, 127, 39)

			elif i[2] == 'ball' or i[2] == 'jumpingBall':
				pygame.draw.circle(screen, (0, 80, 120), (int(i[0]) * 36 + 18, int(i[1]) * 36 + 18), 8) # (63, 72, 204)

			elif  i[2] == 'spawnPoint' or i[2] == 'checkPoint' or i[2] == 'endPoint':
				pygame.draw.rect(screen, (80, 225, 120), (int(i[0]) * 36, int(i[1]) * 36, 36, 36)) # (255, 127, 39)

def createNewFile():
	global counts
	if os.path.isdir('levels'):
		onlyfiles = next(os.walk('levels'))[2]
		counts = len(onlyfiles)

		os.chdir('levels')
	
	file = open('level' + str(counts) + '.npy', 'a+')
	file.close()

def saveChanges(changes, file):
	global counts
	if os.path.isdir('levels'):
		onlyfiles = next(os.walk('levels'))[2]
		counts = len(onlyfiles)

		os.chdir('levels')
	try:
		np.save(file + '.npy', changes, allow_pickle=True, fix_imports=True)# 'level' + str(counts) + '.npy', changes, allow_pickle=True, fix_imports=True)
	except NameError:
		np.save('reserve/reseve.npy', changes, allow_pickle=True, fix_imports=True)# 'level' + str(counts) + '.npy', changes, allow_pickle=True, fix_imports=True)

def returnListOfNames():
	levels = []
	try:
		onlyfiles = next(os.walk('levels'))[2]
		for i in range(0, len(onlyfiles)):
			levels.append('level' + str(i))
	except StopIteration:
		quit()
	# os.chdir('word hardest game')
	return (levels)

def readFile(level):
	# level += '.npy'
	# mas = np.load('levels/' + level).tolist()
	# mas2 = []
	# mas3 = []
	# i = 1
	# l = 1
	# while i < len(mas) - 1:
	# 	# print('this is', mas[i])
	# 	block = []
	# 	if mas[i] == '(':
	# 		block.append(int(mas[i + 1]))
	# 		print('this is', list(mas[i+4]))
	# 		block.append(int(mas[i + 4]))
	# 		if True:
	# 			l = 7
	# 			name = ''
	# 			while mas[i+l] != ')':
	# 				name += mas[i+l]
	# 				l += 1
	# 			block.append(name)
	# 		i += l - 1
	# 	mas2.append(block)
	# 	i += 1
	# i = 0
	# while i < len(mas2):
	# 	if mas2[i] != []:
	# 		mas3.append(mas2[i])
	# 	i += 1
	# 	print (mas3)
	# return mas3
	try:
		mas = np.load('levels/' + level + '.npy', allow_pickle=True).tolist()
	except OSError:
		mas = []
	
	mas2 = []
	mas3 = []

	for obj in mas:
		for i in obj:
			try:
				mas3.append(int(i))

			except ValueError:
				mas3.append(i)
				mas2.append(mas3)
				mas3 = []
	print(mas3)
	# print (mas2)

	return mas2, level


def findElem(mas, elem):
	if mas == []:
		return False
	else:
		for i in mas:
			if i[0] == elem[0] and i[1] == elem[1]:
				return True
	return False

def deleteObj(mas, elem):
	if mas == []:
		return 0
	else:
		i = 0
		while i < len(mas):
			if mas[i][0] == elem[0] and mas[i][1] == elem[1]:
				mas.pop(i)
				return 0
			i += 1

def createButtonsOnLevels(screen, font2):
	names = returnListOfNames()

	levels = []
	i = 0
	while i < len(names):
		levels.append(Button(screen, 100, 100 + i * 75, 500, 50, font=font2, writing=names[i], wchx = 10, writingColor=(0, 0, 0), image=None, color = (122, 122, 122), strokeColor = (0, 0, 0), strokeWidth = 10))
		i += 1
	return levels


def deleteLevel(level):
	try:
		path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'levels/' + level + '.npy')
		os.remove(path)
	except FileNotFoundError:
		print('FileNotFoundError')