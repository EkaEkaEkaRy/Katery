from PIL import ImageColor, Image, ImageDraw

k = None
b = None


# координатная плоскость
def coordinate_plane():
    image = Image.new("RGB", (1200, 800))  # создание изображения
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 1200, 800), fill=ImageColor.getrgb("white"))  # белый экран
    draw.line(((1200, 400, 1195, 405)), (0,0,0))
    draw.line(((600, 0, 600, 800)), (0,0,0))
    draw.line(((0, 400, 1200, 400)), (0,0,0))
    draw.line(((595, 5, 600, 0)), (0,0,0))
    draw.line(((600, 0, 605, 5)), (0,0,0))
    draw.line(((1195, 395, 1200, 400)), (0,0,0))
    draw.line(((1200, 400, 1195, 405)), (0,0,0))
    return image, draw



# линейная функция
def line_asc():
    print('y=k*x+b')
    k = int(input("Введите k:  "))
    b = int(input("Введите b:  "))
    return k,b

def line_f(x_f):
    global k,b
    y_f = k*x_f +b
    return y_f



# квадратичная функция
def quadratic_asc():
    print('y=a*x^2+b*x+c')
    a = int(input("Введите a:  "))
    b = int(input("Введите b:  "))
    c = int(input("Введите c:  "))
    return a, b, с


def quadratic_f(x_f):
    y_f =a*x_f**2+b*x_f+c
    return x_f, y_f




# обратная пропорциональность
def gip_f(x):
    print ('y=k/x')
    k = int(input("Введите k:  "))
    y =k/x
    return x, y


