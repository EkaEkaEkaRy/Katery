import pygame
from random import randint
pygame.init()
gamedisplay = pygame.display.set_mode((1200,800)) # экран размером 800 на 600
pygame.display.set_caption("Параметрически заданные линии")
gamedisplay.fill((255,255,255)) # заливка экрана белым

N = 20

r = 0
g = 0
b = 0
radius = 5

game = True
while game:
    color = (r, g, b)
    events = pygame.event.get() # запрашиваем событие, произошедшее в игре

    for event in events: # берем события по одному
        if event.type == pygame.QUIT: # закрытие окна
            game = False

        if pygame.key.get_pressed()[pygame.K_SPACE]:   # чистая координатная плоскость
            gamedisplay.fill((255, 255, 255))
            pygame.draw.line(gamedisplay, (0, 0, 0), (1200, 400), (1195, 405), 2)
            pygame.draw.line(gamedisplay, (0, 0, 0), (600, 0), (600, 800), 2)
            pygame.draw.line(gamedisplay, (0, 0, 0), (0, 400), (1200, 400), 2)
            pygame.draw.line(gamedisplay, (0, 0, 0), (595, 5), (600, 0), 2)
            pygame.draw.line(gamedisplay, (0, 0, 0), (600, 0), (605, 5), 2)
            pygame.draw.line(gamedisplay, (0, 0, 0), (1195, 395), (1200, 400), 2)
            pygame.draw.line(gamedisplay, (0, 0, 0), (1200, 400), (1195, 405), 2)

    
    '''answer = input("(1)Линейная функция\n(2)Квадратичная функция\n(3)Обратная пропорциональность\n>>>\t")

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    if answer == '1':
        print('y=k*x+b')
        k = float(input("Введите k:  "))
        b = float(input("Введите b:  "))'''
