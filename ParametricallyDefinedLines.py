import pygame
from random import randint
pygame.init()
rule = pygame.font.SysFont('Ink Free', 50)  #название и размер шрифта
rules_start = rule.render("ИНСТРУКЦИЯ",True, (255, 255, 255))
rule = pygame.font.SysFont('Ink Free', 30)
rule_1 = rule.render("Чтобы начертить оси координат, нажмите ЛЕВУЮ КНОПКУ МЫШКИ",True, (255, 255, 255))
rule_2 = rule.render("Чтобы появилась клетка, нажмите ПРАВУЮ КНОПКУ МЫШКИ", True, (255, 255, 255))
rule_3 = rule.render("Чтобы очистить экран, нажмите ENTER", True, (255, 255, 255))
rule_4 = rule.render("Чтобы построить график, нажмите ПРОБЕЛ", True, (255, 255, 255))
rule_5 = rule.render("Для продолжения нажмите ENTER", True, (255, 255, 255))

gamedisplay = pygame.display.set_mode((1200,800)) # экран размером 800 на 600
pygame.display.set_caption("Параметрически заданные линии")

gamedisplay.fill((0,0,0)) # заливка экрана белым
gamedisplay.blit(rules_start, (400, 20))
gamedisplay.blit(rule_1, (20, 100))
gamedisplay.blit(rule_2, (20, 150))
gamedisplay.blit(rule_3, (20, 200))
gamedisplay.blit(rule_4, (20, 250))
gamedisplay.blit(rule_5, (20, 300))

red = 0
green = 0
blue = 0
y = 0

def find_y():
    global y, k, b, a, c
    if i == 1:
        k = k
        b = b
        y = k * x + (b * 20)
    elif i == 2:
        a = a
        b = b
        c = c
        y = (a / 20) * x ** 2 + b * x + (c * 20)
    elif i == 3:
        k = k
        y = (400 * k) / x


game = True
while game:

    x_begin = -600
    x_end = 600
    ox = 0

    N = 0
    color = (red, green, blue)
    events = pygame.event.get() # запрашиваем событие, произошедшее в игре

    for event in events: # берем события по одному
        if event.type == pygame.QUIT: # закрытие окна
            game = False

        if pygame.key.get_pressed()[pygame.K_KP_ENTER]:   # очистка экрана
            gamedisplay.fill((255, 255, 255))



        if pygame.key.get_pressed()[pygame.K_SPACE]:
            answer = input("(1)Линейная функция\n(2)Квадратичная функция\n(3)Обратная пропорциональность\n>>>\t")
            if answer == "1":
                print('y = k * x + b')
                k = float(input('Введите k:\t'))
                b = float(input('Введите b:\t'))
                i = 1
            elif answer == "2":
                print('y = a * x^2 + b * x + c')
                a = float(input('Введите a:\t'))
                b = float(input('Введите b:\t'))
                c = float(input('Введите c:\t'))
                i = 2
            elif answer == "3":
                print('y = k / x')
                k = float(input('Введите k:\t'))
                i = 3

            red = randint(0, 255)
            green = randint(0, 255)
            blue = randint(0, 255)
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