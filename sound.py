import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('assets/images/cat.png')
catx = 10
caty = 10
direction = 'right'

# background music
pygame.mixer.music.load('assets/music/morning.mp3')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

# sfx
sound_beep = pygame.mixer.Sound('assets/sfx/beep1.ogg')

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
            sound_beep.play()
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
            sound_beep.play()
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
            sound_beep.play()
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'
            sound_beep.play()

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)