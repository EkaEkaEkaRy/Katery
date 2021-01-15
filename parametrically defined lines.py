from PDLdef import coordinate_plane, convert, color
from PDLdef import line_f, quadratic_f, gip_f
from PDLdef import image, draw, k, b, a, c, asc, x, x_f, y, y_f, Point


coordinate_plane


game = True

points =[]

start_x = 0
end_x = 1200
x_f = -600


x = start_x

answer = input("(1)Линейная функция\n(2)Квадратичная функция\n(3)Обратная пропорциональность\n>>>\t")
while x <= end_x:
    x+= 0.5
    x_f+= 0.5
    if answer == "1":
        print(line_f(x_f))
    elif answer == "2":
        print(quadratic_f(x_f))
    elif answer == "3":
        print(gip_f(x_f))

    y = (not y_f) + 400
    points.append(Point(x,y))
    for point in points:
        p = convert(point)
        draw.point((p.x, p.y),color())








image.show()