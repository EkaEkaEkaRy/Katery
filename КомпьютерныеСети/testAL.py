from os import system
def algebra_of_logic():
    n = 0  # Счётчик

    with open("Файлы\АлгебраЛогикиТест\question1.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "2":
        n += 1
    system("cls")

    with open("Файлы\АлгебраЛогикиТест\question2.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "6":
        n += 1
    system("cls")

    with open("Файлы\АлгебраЛогикиТест\question3.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "5":
        n += 1
    system("cls")

    with open("Файлы\АлгебраЛогикиТест\question4.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "3":
        n += 1
    system("cls")

    with open("Файлы\АлгебраЛогикиТест\question5.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "346152":
        n += 1
    system("cls")

    with open("Файлы\АлгебраЛогикиТест\question6.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "5":
        n += 1
    system("cls")

    with open("Файлы\АлгебраЛогикиТест\question7.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "1":
        n += 1
    system("cls")

    with open("Файлы\АлгебраЛогикиТест\question8.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "7":
        n += 1
    system("cls")

    with open("Файлы\АлгебраЛогикиТест\question9.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "9":
        n += 1
    system("cls")

    with open("Файлы\АлгебраЛогикиТест\question10.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "2":
        n += 1
    system("cls")

    if n>7:  #Расчёт оценки
        grade = "5"
    elif n>5:
        grade = "4"
    elif n>3:
        grade = "3"
    else:
        grade = "2"

    print(f"Ваш результат: {n*10}%\nВаша оценка: {grade}")