lines = int(input('Введите количество строк\n>>>\t'))
print('Введите код')
program =[]
symbols = []
num=0

for i in range(lines): # ввод сторок программы
    str = input('>>>\t')
    program.append(str)

for str in program: # берется одна строка

    for symbol in range(len(str)): # список из букв строки
        symbols.append(str[symbol])

    print(symbols) # временно

    for s in range(len(symbols)):
        num+=1

        if symbols[num-1] == ' ': # убирает пробелы
            if symbols[num] == ' ':
                symbols.pop(num-1)
                num -= 1

        elif symbols[num-1] == '"' or symbols[num-1] == "'":
            continue
            num += 1
            continue
            while symbols[num-1] != '"' or symbols[num-1] != "'":
                num += 1

        elif symbols[num-1] == '#': # убирает комментарии
            symbols.pop(num-1)
            num -= 1
            while num != len(symbols):
                print(symbols)
                symbols.pop(num - 1)
                num+=1
            break

    print(''.join(symbols)) # вывод стороки






