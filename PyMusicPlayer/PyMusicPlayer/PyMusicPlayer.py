#import pygame.mixer
import pygame, sys
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((320, 240))
screen = pygame.display.get_surface()

btnPlay = pygame.image.load('img\sprPlayWhite.png')
btnPause = pygame.image.load('img\sprPauseWhite.png')
btnStop = pygame.image.load('img\sprStopWhite.png')

while True:

    window.blit(btnPlay, (50, 100))

    for event in pygame.event.get():
        if event.type == quit or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
    pygame.display.update()