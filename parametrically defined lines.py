from PIL import Image, ImageColor, ImageDraw
image = Image.new("RGB", (1200, 800)) # создание изображения
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, 1200, 800), fill=ImageColor.getrgb("white")) # белый экран
draw.line(((600,0,600,800)), fill=ImageColor.getrgb("grey"))
draw.line(((0,400,1200,400)), fill=ImageColor.getrgb("grey"))
draw.line(((595,5,600,0)), fill=ImageColor.getrgb("grey"))
draw.line(((600,0,605,5)), fill=ImageColor.getrgb("grey"))
draw.line(((1195,395,1200,400)), fill=ImageColor.getrgb("grey"))
draw.line(((1200,400,1195,405)), fill=ImageColor.getrgb("grey"))


def line_f(x):
    return k*x+b
k= int(input("Введите k:  "))
b= int(input("Введите b:  "))
image.show()