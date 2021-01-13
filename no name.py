def line_f(x_f):
    print('y=k*x+b')
    k = int(input("Введите k:  "))
    b = int(input("Введите b:  "))
    y_f = k*x_f +b
    return y_f


print(line_f(5))