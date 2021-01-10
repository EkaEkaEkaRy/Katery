from PIL import Image, ImageColor, ImageDraw
image = Image.new("RGB", (1200, 800)) # создание изображения
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, 1200, 800), fill=ImageColor.getrgb("white")) # белый экран
# координатная плоскость
draw.line(((600,0,600,800)), fill=ImageColor.getrgb("grey"))
draw.line(((0,400,1200,400)), fill=ImageColor.getrgb("grey"))
draw.line(((595,5,600,0)), fill=ImageColor.getrgb("grey"))
draw.line(((600,0,605,5)), fill=ImageColor.getrgb("grey"))
draw.line(((1195,395,1200,400)), fill=ImageColor.getrgb("grey"))
draw.line(((1200,400,1195,405)), fill=ImageColor.getrgb("grey"))

game = True

class grafic():
    def __init__(self):
        self.start_x=0
        self.end_x=1200
        self.points =[]


    # линейная функция
    def line_f(self):
        print ('y=k*x+b')
        k= int(input("Введите k:  "))
        b= int(input("Введите b:  "))
        x=self.start_x
        while x<=self.end_x:
            y = k*x+b
            self.points.append((x,y))
            x+=0.1
        for i in self.points:
            draw.point((i),(255,0,0))



    # квадратичная функция
    def quadratic_f(self):
        print ('y=a*x^2+b*x+c')
        a= int(input("Введите a:  "))
        b= int(input("Введите b:  "))
        c = int(input("Введите c:  "))
        x = self.start_x
        y =a*x**2+b*x+c


    # обратная пропорциональность
    def gip_f(self):
        print ('y=k/x')
        k = int(input("Введите k:  "))
        x = self.start_x
        y =k/x

function1=grafic()
print(function1.line_f())

image.show()