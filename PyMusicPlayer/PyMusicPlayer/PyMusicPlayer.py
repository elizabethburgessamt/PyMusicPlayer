#import pygame.mixer
import pygame, sys, os
from pygame.locals import *

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((320, 240))
screen = pygame.display.get_surface()

btnPlay = pygame.image.load('img\sprPlayWhite.png')
btnPause = pygame.image.load('img\sprPauseWhite.png')
btnStop = pygame.image.load('img\sprStopWhite.png')

BASICFONT = pygame.font.Font(None, 12)

debugMode = True

if debugMode == True:
    pthMusicDefault = 'C:\\Users\\Hectaimon\\Music'
else:
    pthMusicDefault = '\\media\\'

filesMusic = [f for f in os.listdir(pthMusicDefault) if os.path.isfile(os.path.join(pthMusicDefault, f))]
currentSong = filesMusic[1]
pygame.mixer.music.load(os.path.join(pthMusicDefault, currentSong))

def main():
    
    window.blit(btnPlay, (50, 100))
    btnActive = 'Stop'

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
        
        makeText(currentSong, Color(255, 255, 255, 255), Color(0, 0, 0, 0), 100, 100)

        if 50 < mouseX < 90 and 100 < mouseY < 140 and mouseClicked == True:
            if btnActive == 'Stop':
                window.fill(Color(0, 0, 0, 0))
                window.blit(btnPause, (50, 100))
                loadSong(filesMusic)
                btnActive = 'Play'
            elif btnActive == 'Play':
                btnActive = 'Pause'
                window.fill(Color(0, 0, 0, 0))
                window.blit(btnPlay, (50, 100))
                pauseSong()
            elif btnActive == 'Pause':
                window.fill(Color(0, 0, 0, 0))
                window.blit(btnPause, (50, 100))
                playSong(btnActive)
                btnActive = 'Play'
        pygame.display.update()

        
        
def loadSong(filesMusic):
    #load song

    #for f in filesMusic:
    #pygame.mixer.music.load(os.path.join(pthMusicDefault, filesMusic[1]))
    pygame.mixer.music.play()

def playSong(btnActive):
    if btnActive == "Pause":
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.play()

def pauseSong():
    pygame.mixer.music.pause()

def stopSong():
    pygame.mixer.music.stop()

def makeText(text, color, bgcolor, top, left):
    textSurf = BASICFONT.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect = top, left
    return (textSurf, textRect)

if __name__ == '__main__':
    main()