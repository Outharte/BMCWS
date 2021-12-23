import pygame as pg
import sys, csv
from pygame.locals import *

pg.init()
mainClock = pg.time.Clock()

wWidth = 400
wHeight = 700
screen = pg.display.set_mode((wWidth, wHeight), 0, 32)
pg.display.set_caption('Testrun')

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

text = ''

basicFont = pg.font.SysFont(None, 40)

data = []
with open('SET.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        data.extend(line)

puzz = data[37]
target = data[0] + data[1]
subpuzz0 = data[4]
subpuzz1 = data[5]
subpuzz2 = data[6]
subpuzz3 = data[7]

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                print(text)
                if text.upper() == data[38]:
                    print('success 0')
                    subpuzz0 = data[38]
                if text.upper() == data[39]:
                    print('success 1')
                    subpuzz1 = data[39]
                if text.upper() == data[40]:
                    print('success 2')
                    subpuzz2 = data[40]
                if text.upper() == data[41]:
                    print('success 3')
                    subpuzz3 = data[41]
                if text.upper() == target.upper():
                    print('success ')
                    puzz = target
                text=''
            elif event.key == pg.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode


    input_box = pg.Rect(wWidth / 2, wHeight - 100, 140, 32)

    text0 = basicFont.render(puzz, True, BLACK, WHITE)
    text0Rect = text0.get_rect()
    text0Rect.centerx = screen.get_rect().centerx
    text0Rect.centery = screen.get_rect().centery

    text1 = basicFont.render(subpuzz0, True, BLACK, WHITE)
    text1Rect = text1.get_rect()
    text1Rect.centerx = 125
    text1Rect.centery = 100

    text2 = basicFont.render(subpuzz1, True, BLACK, WHITE)
    text2Rect = text2.get_rect()
    text2Rect.centerx = 275
    text2Rect.centery = 100

    text3 = basicFont.render(subpuzz2, True, BLACK, WHITE)
    text3Rect = text3.get_rect()
    text3Rect.centerx = 75
    text3Rect.centery = 300

    text4 = basicFont.render(subpuzz3, True, BLACK, WHITE)
    text4Rect = text4.get_rect()
    text4Rect.centerx = 325
    text4Rect.centery = 300

    screen.fill(WHITE)

    if subpuzz0 == data[38] and subpuzz1 == data[39] and subpuzz2 == data[40] and subpuzz3 == data[41]:
        screen.blit(text0, text0Rect)
    screen.blit(text1, text1Rect)
    screen.blit(text2, text2Rect)
    screen.blit(text3, text3Rect)
    screen.blit(text4, text4Rect)

    txt_surface = basicFont.render(text, True, BLACK)
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    pg.draw.rect(screen, BLUE, input_box, 2)

    pg.display.flip()
    mainClock.tick(40)
