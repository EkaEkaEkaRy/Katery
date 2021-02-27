import pygame
from random import randint
pygame.init()
gamedisplay = pygame.display.set_mode((800,600)) # экран размером 800 на 600
gamedisplay.fill((255,255,255)) # заливка экрана желтым
# координатная плоскость
gamedisplay.line(((1200, 400, 1195, 405)), (0, 0, 0))
gamedisplay.line(((600, 0, 600, 800)), (0, 0, 0))
gamedisplay.line(((0, 400, 1200, 400)), (0, 0, 0))
gamedisplay.line(((595, 5, 600, 0)), (0, 0, 0))
gamedisplay.line(((600, 0, 605, 5)), (0, 0, 0))
gamedisplay.line(((1195, 395, 1200, 400)), (0, 0, 0))
gamedisplay.line(((1200, 400, 1195, 405)), (0, 0, 0))

r = 0
g = 0
b = 0
color = (r,g,b)
radius = 5

game = True
while game:
    color = (r, g, b)
    events = pygame.event.get() # запрашиваем событие, произошедшее в игре

    for event in events: # берем события по одному
        if event.type == pygame.QUIT: # закрытие окна
            game = False

