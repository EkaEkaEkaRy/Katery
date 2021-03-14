import pygame
from random import randint
pygame.init()
gamedisplay = pygame.display.set_mode((1200,800)) # экран размером 800 на 600
pygame.display.set_caption("Параметрически заданные линии")
gamedisplay.fill((255,255,255)) # заливка экрана белым

r = 0
g = 0
b = 0

game = True
while game:
    N = 0
    color = (r, g, b)
    events = pygame.event.get() # запрашиваем событие, произошедшее в игре

    for event in events: # берем события по одному
        if event.type == pygame.QUIT: # закрытие окна
            game = False

        if pygame.key.get_pressed()[pygame.K_SPACE]:   # очистка экрана
            gamedisplay.fill((255, 255, 255))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:  # координатная плоскость
                pygame.draw.line(gamedisplay, (0, 0, 0), (1200, 400), (1195, 405), 1)
                pygame.draw.line(gamedisplay, (0, 0, 0), (600, 0), (600, 800), 1)
                pygame.draw.line(gamedisplay, (0, 0, 0), (0, 400), (1200, 400), 1)
                pygame.draw.line(gamedisplay, (0, 0, 0), (595, 5), (600, 0), 1)
                pygame.draw.line(gamedisplay, (0, 0, 0), (600, 0), (605, 5), 1)
                pygame.draw.line(gamedisplay, (0, 0, 0), (1195, 395), (1200, 400), 1)
                pygame.draw.line(gamedisplay, (0, 0, 0), (1200, 400), (1195, 405), 1)
                while N <= 1200:
                    pygame.draw.line(gamedisplay, (0, 0, 0), (N, 399), (N, 401), 1)
                    pygame.draw.line(gamedisplay, (0, 0, 0), (599, N), (601, N), 1)
                    N += 20

            if event.button == pygame.BUTTON_RIGHT: # клетка
                while N <= 1200:
                    pygame.draw.line(gamedisplay, (200, 200, 200), (N, 0), (N, 800), 1)
                    pygame.draw.line(gamedisplay, (200, 200, 200), (0, N), (1200, N), 1)
                    N += 20

            if event.type == pygame.MOUSEWHEEL:
                k = 1
                b = 0
                r = randint(0, 255)
                g = randint(0, 255)
                b = randint(0, 255)
                pygame.draw.line(gamedisplay, color, (1200, k*(-600)+b*20), (0, k*600+b*20), 2)
                print("1")

    """answer = input("(1)Линейная функция\n(2)Квадратичная функция\n(3)Обратная пропорциональность\n>>>\t")

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    if answer == '1':
        print('y=k*x+b')
        k = float(input("Введите k:  "))
        b = float(input("Введите b:  "))
        pygame.draw.line(gamedisplay, color, (1200, k*(-600)+b*20), (0, k*600+b*20), 2)"""



    pygame.display.update()
pygame.quit()