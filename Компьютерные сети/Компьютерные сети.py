from os import system
game = True
while True:
    answer = input("(1)Изучить учебный материал\n(2)Пройти тест\n>>>\t")
    system("cls")
    if answer == "1":
        while game:
            with open("содержание.txt", 'r', encoding='utf-8') as text:
                print(text.read())
            answer = input(">>>\t").lower()
            system("cls")
            if answer == "1":
                with open("АлгебраЛогики.txt", 'r', encoding='utf-8') as text:
                    print(text.read())
                print("*"*50)
                print()



            elif answer == "назад":
                game = False






    elif answer == "2":
        with open("АлгебраЛогики.txt", 'r', encoding='utf-8') as text:
            print(text.read())
