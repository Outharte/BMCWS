import pygame, sys, csv
from pygame.locals import *

pygame.init()

windowSurface = pygame.display.set_mode((400, 700), 0, 32)
pygame.display.set_caption('Testrun')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

basicFont = pygame.font.SysFont(None, 40)

data = []
with open('SET.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        data.extend(line)


text = basicFont.render(data[0]+data[1], True, BLACK, WHITE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

text1 = basicFont.render(data[4], True, BLACK, WHITE)
text1Rect = text1.get_rect()
text1Rect.centerx = 125
text1Rect.centery = 100

text2 = basicFont.render(data[5], True, BLACK, WHITE)
text2Rect = text2.get_rect()
text2Rect.centerx = 275
text2Rect.centery = 100

text3 = basicFont.render(data[6], True, BLACK, WHITE)
text3Rect = text3.get_rect()
text3Rect.centerx = 75
text3Rect.centery = 300

text4 = basicFont.render(data[7], True, BLACK, WHITE)
text4Rect = text4.get_rect()
text4Rect.centerx = 325
text4Rect.centery = 300

windowSurface.fill(WHITE)


#pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

pixArray = pygame.PixelArray(windowSurface)
pixArray[380][680] = BLACK
del pixArray

windowSurface.blit(text, textRect)
windowSurface.blit(text1, text1Rect)
windowSurface.blit(text2, text2Rect)
windowSurface.blit(text3, text3Rect)
windowSurface.blit(text4, text4Rect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
