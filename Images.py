import pygame

w, h = 400, 400
gridW, gridH = 300, 300
padding = 50

pygame.init()
screen = pygame.display.set_mode((w, h))
done = False

clock = pygame.time.Clock()

#surface = pygame.Surface((100, 100), pygame.SRCALPHA)
imageX = pygame.image.load('cross.png')
imageY = pygame.image.load('zero.png')
#imageEmpty = pygame.image.load('test3.png')
centerX = w / 2 - padding
centerY = h / 2 - padding
black = (0, 0, 0)
white = (255, 255, 255)

EMPTY = 0
MOVE_X = 1
MOVE_Y = 2

iSize = 100

dX = [-iSize,   0,  iSize, -iSize, 0, iSize, -iSize,  0, iSize]
dY = [-iSize, -iSize, -iSize,   0, 0,  0,  iSize, iSize, iSize]


pos = [EMPTY for i in range(0, 10)]
pos[2] = MOVE_X
pos[4] = MOVE_Y
pos[6] = MOVE_Y

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
           (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
               done = True
    screen.fill(black)

    pygame.draw.rect(screen, white, pygame.Rect(padding, padding, gridW, gridH))
    
    for i in range(0, 9):
        x = centerX + dX[i]
        y = centerY + dY[i]
        if pos[i] == MOVE_X:
            screen.blit(imageX, (x, y))
        elif pos[i] == MOVE_Y:
            screen.blit(imageY, (x, y))

    pygame.display.flip()
    clock.tick(60)
