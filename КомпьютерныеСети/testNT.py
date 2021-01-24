from PIL import Image
from os import system
def network_topologies():
    n = 0
    image = Image.open('Картинки\ячеистая.png')
    image.show()
    with open("Файлы\ТопологииСетей\question1.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "2":
        n += 1
    system("cls")

    image = Image.open('Картинки\шина.png')
    image.show()
    with open("Файлы\ТопологииСетей\question2.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "3":
        n += 1
    system("cls")

    image = Image.open('Картинки\иерархическая.png')
    image.show()
    with open("Файлы\ТопологииСетей\question3.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "6":
        n += 1
    system("cls")

    image = Image.open('Картинки\полносвязная.png')
    image.show()
    with open("Файлы\ТопологииСетей\question4.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "1":
        n += 1
    system("cls")

    image = Image.open('Картинки\звезда.gif')
    image.show()
    with open("Файлы\ТопологииСетей\question5.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "4":
        n += 1
    system("cls")

    image = Image.open('Картинки\кольцо.jpg')
    image.show()
    with open("Файлы\ТопологииСетей\question6.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "5":
        n += 1
    system("cls")

    if n>5:  #Расчёт оценки
        grade = "5"
    elif n>3:
        grade = "4"
    elif n>2:
        grade = "3"
    else:
        grade = "2"

    print(f"Ваш результат: {(n*100)//6}%\nВаша оценка: {grade}")