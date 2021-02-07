lines = int(input('Введите количество строк\n>>>\t'))
print('Введите код')
program =[]
symbols = []
string = []
letter = False

for i in range(lines): # ввод сторок программы
    str = input('>>>\t')
    program.append(str)

for str in program: # берется одна строка

    for symbol in range(len(str)): # список из букв строки
        symbols.append(str[symbol])

    for s in range(len(symbols)):

        if letter:   # буквы в кавычках
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

        else:
            string.append(symbols[s])


    print(''.join(string)) # вывод стороки
    string = []
    symbols = []





