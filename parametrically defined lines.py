from PDLdef import color, condition
from PDLdef import line_f, quadratic_f, gip_f
from PDLdef import k, b, a, c, asc, x, x_f, y, y_f
from PIL import ImageColor, Image, ImageDraw


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
    asc = True
    start_x = 0
    end_x = 1200
    x_f = -600.5
    x2 = start_x



    answer = input("(1)Линейная функция\n(2)Квадратичная функция\n(3)Обратная пропорциональность\n>>>\t")
    condition(answer)
    y2 = 400 - y_f
    
    while x2 <= end_x:
        x1 = x2
        y1 = y2
        x_f+= 0.5
        condition(answer)
        x2 += 0.5
        y2 = 400 - y_f
        draw.line((x1, y1, x2, y2), (color()), 2)


    image.show()
    answer = input("Хотите начертить ещё одну линию?\t").lower()
    if answer == "да" or "yes":
        game = True
    else:
        game = False