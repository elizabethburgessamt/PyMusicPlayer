#import pygame.mixer
import pygame, sys, os
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((320, 240))
screen = pygame.display.get_surface()

btnPlay = pygame.image.load('img\sprPlayWhite.png')
btnPause = pygame.image.load('img\sprPauseWhite.png')
btnStop = pygame.image.load('img\sprStopWhite.png')

debugMode = True

if debugMode == True:
    pthMusicDefault = 'C:\\Users\\Hectaimon\\Music'
else:
    pthMusicDefault = '\\media\\'

def main():
    filesMusic = [f for f in os.listdir(pthMusicDefault) if os.path.isfile(os.path.join(pthMusicDefault, f))]
    
    window.blit(btnPlay, (50, 100))

    mouseX = 0
    mouseY = 0

    while True:
        mouseClicked = False
        

        for event in pygame.event.get():
            
            if event.type == quit or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mouseX, mouseY = event.pos
                mouseClicked = True
        pygame.display.update()

if __name__ == '__main__':
    main()