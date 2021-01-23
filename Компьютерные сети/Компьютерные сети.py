from os import system
while True:
    game = True
    answer = input("(1)Изучить учебный материал\n(2)Пройти тест\n>>>\t")
    system("cls") #Очистить консоль
    if answer == "1": #Изучение учебного материала
        while game:
            with open("содержание.txt", 'r', encoding='utf-8') as text: #Содержание
                print(text.read())
            answer = input(">>>\t").lower()
            system("cls") #Очистить консоль
            if answer == "1": #Алгебра логики
                with open("АлгебраЛогики.txt", 'r', encoding='utf-8') as text:
                    print(text.read())
                print("*"*50)
                print()
            elif answer == "2": #Компьютерные сети
                with open("КомпьютерныеСети.txt", 'r', encoding='utf-8') as text:
                    print(text.read())
                print("*"*50)
                print()
            elif answer == "3": #Топологии сетей
                with open("ТопологииСетей.txt", 'r', encoding='utf-8') as text:
                    print(text.read())
                print("*"*50)
                print()
            elif answer == "назад": #Вернуться к меню
                game = False #Завершение цикла "содержание"
    elif answer == "2": #Тест
        n = None #Счётчик
        with open("question1.txt", 'r', encoding='utf-8') as text:
            print(text.read())
        text_answer = input(">>>\t")
