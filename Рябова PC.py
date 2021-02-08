lines = int(input('Введите количество строк\n>>>\t'))
print('Введите код')
program =[] # список строк в программе
symbols = [] # список символов в строке
string = [] # список симколов для вывода
letter = False # для букв в кавычках
space = False # для пробелов в начале

for i in range(lines): # ввод сторок программы
    str = input('>>>\t')
    program.append(str) # добавление строк в список

for str in program: # берется одна строка

    for symbol in range(len(str)): # список из букв строки
        symbols.append(str[symbol]) # добавление букв в список

    for s in range(len(symbols)): # основная часть

        if space: # пробелы в начале строки
            if symbols[s] != ' ': # поробелов больше нет
                space = False
                string.append(symbols[s])
            else:
                string.append(symbols[s])

        elif s == 1 and symbols[0] == ' ': # пробел стоит в начале
            space = True
            string.append(symbols[s])

        elif letter:   # буквы в кавычках
            if symbols[s] == '"' or symbols[s] == "'": # конец кавычек
                letter = False
                string.append(symbols[s])
            else:
                string.append(symbols[s])

        elif symbols[s] == '"' or symbols[s] == "'": # кавычки
            letter = True
            string.append(symbols[s])

        elif symbols[s] == ' ': # убирает пробелы
            if symbols[s+1] == ' ':
                None
            else:
                string.append(symbols[s])

        elif symbols[s] == '#': # убирает комментарии
            break

        else: # добавление оставшихся символов в список
            string.append(symbols[s])

    print(''.join(string)) # вывод стороки
    # очистка списка
    string = []
    symbols = []