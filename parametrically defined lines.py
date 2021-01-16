from PDLdef import coordinate_plane, color, condition
from PDLdef import line_f, quadratic_f, gip_f
from PDLdef import image, draw, k, b, a, c, asc, x, x_f, y, y_f


coordinate_plane


game = True

while game:
    asc = True
    start_x = 0
    end_x = 1200
    x_f = -600.5
    x2 = start_x



    answer = input("(1)Линейная функция\n(2)Квадратичная функция\n(3)Обратная пропорциональность\n>>>\t")
    """
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
    """


    image.show()
    answer = input("Хотите начертить ещё одну линию?\t").lower()
    if answer == "да" or "yes":
        game = True
    else:
        game = False