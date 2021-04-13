import pygame
from random import randint, choice
pygame.init()
gamedisplay = pygame.display.set_mode((1200,800)) # экран размером 800 на 600
pygame.display.set_caption("Параметрически заданные линии")
gamedisplay.fill((255,255,255)) # заливка экрана белым

rgb = [(234, 46, 17), (69, 212, 196)]
y = 0

def find_y():
    global y
    if i == 1:
        k = 1
        b = 0
        y = k * x + (b * 20)
    elif i == 2:
        a = 1
        b = 0
        c = 0
        y = (a / 20) * x ** 2 + b * x + (c * 20)
    elif i == 3:
        k = 10
        y = (400 * k) / x


game = True
while game:

    x_begin = -600
    x_end = 600
    ox = 0

    N = 0

    events = pygame.event.get() # запрашиваем событие, произошедшее в игре

    for event in events: # берем события по одному
        if event.type == pygame.QUIT: # закрытие окна
            game = False

        if pygame.key.get_pressed()[pygame.K_SPACE]:   # очистка экрана
            gamedisplay.fill((255, 255, 255))



        if pygame.key.get_pressed()[pygame.K_1]:
            #answer = input("(1)Линейная функция\n(2)Квадратичная функция\n(3)Обратная пропорциональность\n>>>\t")
            answer = randint(1, 3)
            if answer == 1:
                i = 1
            elif answer == 2:
                i = 2
            elif answer == 3:
                i = 3

            color = choice(rgb)
            x = x_begin
            find_y()
            while x <= x_end:
                ox2 = ox
                ox += 0.1
                x2 = x
                y2 = y
                x += 0.1
                find_y()
                pygame.draw.line(gamedisplay, color, (ox2, 400 - y2), (ox, 400 - y), 2)


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
                    if N != 600:
                        pygame.draw.line(gamedisplay, (200, 200, 200), (N, 0), (N, 800), 1)
                    if N != 400:
                        pygame.draw.line(gamedisplay, (200, 200, 200), (0, N), (1200, N), 1)
                    N += 20



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