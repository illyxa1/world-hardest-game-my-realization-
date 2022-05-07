import pygame
pygame.init()

size = (700, 500)
UNIT = 25

clock = pygame.time.Clock()
FPS = 60
# colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BEAUTIFULRED = (255, 20, 20)
GREEN = (0, 255, 0)
BEAUTIFULGREEN = (61, 122, 61)
CYAN = (0, 122, 122)
GREY = (122, 122, 122)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# fonts
font = pygame.font.Font('fonts/INVASION2000.TTF', 40)
font2 = pygame.font.Font('fonts/INVASION2000.TTF', 50)
font3 = pygame.font.Font('fonts/INVASION2000.TTF', 55)
font4 = pygame.font.Font('fonts/INVASION2000.TTF', 25)

# button images
wallImage = pygame.image.load('images/button sprites/wall.bmp')
wallImage.set_colorkey((255, 255, 255))

trashBinImage = pygame.image.load('images/button sprites/delete.bmp')
trashBinImage.set_colorkey((255, 255, 255))

ballImage = pygame.image.load('images/button sprites/ball.bmp')
ballImage.set_colorkey((255, 255, 255))

jumpingBallImage = pygame.image.load('images/button sprites/jumpingBall.bmp')
jumpingBallImage.set_colorkey((255, 255, 255))

newImage = pygame.image.load('images/button sprites/new.bmp')
newImage.set_colorkey((255, 0, 0))

saveImage = pygame.image.load('images/button sprites/save.bmp')
saveImage.set_colorkey((255, 0, 0))

emptyImage = pygame.image.load('images/button sprites/empty.bmp')
emptyImage.set_colorkey((255, 0, 0))

choiceLevelImage = pygame.image.load('images/button sprites/choiceLvl.bmp')
choiceLevelImage.set_colorkey((255, 0, 0))

spawnImage = pygame.image.load('images/button sprites/spawn.bmp')
spawnImage.set_colorkey((255, 255, 255))

spawnPointImage = pygame.image.load('images/button sprites/spawnPoint.bmp')
spawnPointImage.set_colorkey((255, 255, 255))

endPointImage = pygame.image.load('images/button sprites/endPoint.bmp')

checkPointImage = pygame.image.load('images/button sprites/checkPoint.bmp')
checkPointImage.set_colorkey((255, 255, 255))

clearAllImage = pygame.image.load('images/button sprites/clearAll.bmp')
clearAllImage.set_colorkey((255, 0, 0))
# creator edites
mas = []

