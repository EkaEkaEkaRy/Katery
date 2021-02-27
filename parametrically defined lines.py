from PIL import ImageColor, Image, ImageDraw
from random import randint

r=None
g=None
b=None



def color():
    r = randint(1,254)
    g = randint(1,254)
    b = randint(1,254)
    return r, g, b


# линейная функция
def line_f(x_f):
    y_f = k*x_f+b
    return y_f

# квадратичная функция
def quadratic_f(x_f):
    global asc
    if asc:
        global a, b, c
        print('y=a*x^2+b*x+c')
        a = float(input("Введите a:  "))
        b = float(input("Введите b:  "))
        c = float(input("Введите c:  "))
        asc = False
    y_f = a*x_f**2+b*x_f+c
    return y_f

# обратная пропорциональность
def gip_f(x_f):
    global asc
    if asc:
        global k
        print ('y=k/x')
        k = float(input("Введите k:  "))
        asc = False
    y_f = k/x_f
    return y_f


image = Image.new("RGB", (1200, 800))  # создание изображения
draw = ImageDraw.Draw(image)
# координатная плоскость
draw.rectangle((0, 0, 1200, 800), fill=ImageColor.getrgb("white"))  # белый экран
draw.line(((1200, 400, 1195, 405)), (0,0,0))
draw.line(((600, 0, 600, 800)), (0,0,0))
draw.line(((0, 400, 1200, 400)), (0,0,0))
draw.line(((595, 5, 600, 0)), (0,0,0))
draw.line(((600, 0, 605, 5)), (0,0,0))
draw.line(((1195, 395, 1200, 400)), (0,0,0))
draw.line(((1200, 400, 1195, 405)), (0,0,0))


game = True

while game:
    x2 = 0
    x = -600

    answer = input("(1)Линейная функция\n(2)Квадратичная функция\n(3)Обратная пропорциональность\n>>>\t")
    color()
    if answer == '1':
        print('y=k*x+b')
        k = float(input("Введите k:  "))
        b = float(input("Введите b:  "))
        y2 = 400-(k*x+b)

        while x <= 600:
            x += 0.5
            x1 = x2
            y1 = y2
            x2 += 0.5
            y2 = 400 - (k * x + b)
            draw.line((x1, y1, x2, y2), (r, g, b), 2)

    image.show()
    answer = input("Хотите начертить ещё одну линию?\t").lower()
    if answer == "да" or "yes":
        game = True
    else:
        game = False