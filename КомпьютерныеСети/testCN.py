from os import system
def computer_network():
    n = 0  # Счётчик
    with open("Файлы\КомпьютерныеСетиТест\question1.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "2":
        n += 1
    system("cls")

    with open("Файлы\КомпьютерныеСетиТест\question2.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "2":
        n += 1
    system("cls")

    with open("Файлы\КомпьютерныеСетиТест\question3.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "1":
        n += 1
    system("cls")

    with open("Файлы\КомпьютерныеСетиТест\question4.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "3":
        n += 1
    system("cls")

    with open("Файлы\КомпьютерныеСетиТест\question5.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "2":
        n += 1
    system("cls")

    with open("Файлы\КомпьютерныеСетиТест\question6.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "2":
        n += 1
    system("cls")

    with open("Файлы\КомпьютерныеСетиТест\question7.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "4":
        n += 1
    system("cls")

    with open("Файлы\КомпьютерныеСетиТест\question8.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "1":
        n += 1
    system("cls")

    with open("Файлы\КомпьютерныеСетиТест\question9.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "2":
        n += 1
    system("cls")

    with open("Файлы\КомпьютерныеСетиТест\question10.txt", 'r', encoding='utf-8') as text:
        print(text.read())
    text_answer = input(">>>\t")
    if text_answer == "3":
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