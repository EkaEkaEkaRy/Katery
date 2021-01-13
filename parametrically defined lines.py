from PIL import Image, ImageColor, ImageDraw
from random import randint
from PDLdef import line_asc, line_f

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


game = True



points =[]
r = randint(1,254)
g = randint(1,254)
b = randint(1,254)

k = None
b = None

start_x = 0
end_x = 1200
x_f = -600


x = start_x

answer = input("(1)Линейная функция\n(2)Квадратичная функция\n(3)Обратная пропорциональность\n>>>\t")
if answer == "1":
    line_asc()
    print(line_f(5))


while x <= end_x:
    x+= 0.5
    x_f+= 0.5
    if answer == 1:
        line_f(x_f)
        y = 400 - y_f
        points.append(x,y)
for point in points:
    draw.point((point),(r,g,b))








image.show()