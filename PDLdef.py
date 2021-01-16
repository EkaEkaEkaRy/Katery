from PIL import ImageColor, Image, ImageDraw
from random import randint


k = None
b = None
a = None
c = None
y_f = None
y = None
x_f = None
x = None
asc = True

def color():
    r = randint(1,254)
    g = randint(1,254)
    b = randint(1,254)
    return r, g, b


image = Image.new("RGB", (1200, 800))  # создание изображения
draw = ImageDraw.Draw(image)
# координатная плоскость
def coordinate_plane():
    draw.rectangle((0, 0, 1200, 800), fill=ImageColor.getrgb("white"))  # белый экран
    draw.line(((1200, 400, 1195, 405)), (0,0,0))
    draw.line(((600, 0, 600, 800)), (0,0,0))
    draw.line(((0, 400, 1200, 400)), (0,0,0))
    draw.line(((595, 5, 600, 0)), (0,0,0))
    draw.line(((600, 0, 605, 5)), (0,0,0))
    draw.line(((1195, 395, 1200, 400)), (0,0,0))
    draw.line(((1200, 400, 1195, 405)), (0,0,0))



# линейная функция
def line_f(x_f):
    global asc
    if asc:
        global k, b
        print('y=k*x+b')
        k = float(input("Введите k:  "))
        b = float(input("Введите b:  "))
        asc = False
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



def condition(answer):
    if answer == "1":
        print(line_f(x_f))
    elif answer == "2":
        print(quadratic_f(x_f))
    elif answer == "3":
        print(gip_f(x_f))
