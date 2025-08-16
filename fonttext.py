import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Font Text Test')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

font_obj = pygame.font.Font('assets/fonts/pixelifysans.ttf', 32)
text_surface = font_obj.render('Font Text Testção', True, GREEN, BLUE)
text_rect = text_surface.get_rect()
text_rect.center = (200, 150)

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(text_surface, text_rect)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()