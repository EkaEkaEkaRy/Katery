from PIL import Image
from os import system
from testAL import algebra_of_logic
from testCN import computer_network
from testNT import network_topologies
while True:
    game = True
    answer = input("(1)Изучить учебный материал\n(2)Пройти тест\n>>>\t")
    system("cls") #Очистить консоль

    if answer == "1": #Изучение учебного материала
        while game:
            with open("Файлы\содержание.txt", 'r', encoding='utf-8') as text: #Содержание
                print(text.read())
            answer = input(">>>\t").lower()
            system("cls") #Очистить консоль

            if answer == "1": #Алгебра логики
                with open("Файлы\АлгебраЛогики.txt", 'r', encoding='utf-8') as text:
                    print(text.read())
                print("*"*50)
                print()

            elif answer == "2": #Компьютерные сети
                with open("Файлы\КомпьютерныеСети.txt", 'r', encoding='utf-8') as text:
                    print(text.read())
                print("*"*50)
                print()

            elif answer == "3": #Топологии сетей
                image = Image.open('Картинки\топологии.jpg')
                image.show()
                with open("Файлы\ТопологииСетей.txt", 'r', encoding='utf-8') as text:
                    print(text.read())
                print("*"*50)
                print()

            elif answer == "в начало": #Вернуться в начало
                game = False #Завершение цикла "содержание"

            if answer != "в начало":
                answer = input(">>>\t").lower()
                if answer == "в начало": #Вернуться в начало
                    game = False #Завершение цикла "содержание"

    elif answer == "2": #Тест
        while game:
            with open("Файлы\содержание.txt", 'r', encoding='utf-8') as text:  # Содержание
                print(text.read())
            answer = input(">>>\t").lower()
            system("cls")  # Очистить консоль

            if answer == "1":
                algebra_of_logic()

            elif answer == "2":
                computer_network()

            elif answer == "3":
                network_topologies()

            elif answer == "в начало": #Вернуться в начало
                game = False #Завершение цикла "тест"

            if answer != "в начало":
                answer = input(">>>\t").lower()
                if answer == "в начало":  # Вернуться в начало
                    game = False  # Завершение цикла "содержание"
