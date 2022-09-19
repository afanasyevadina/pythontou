# Программа получает ввод чисел X A B, затем выводит значение Y согласно
# y = (5 * x^2) / (6 * (a + b)^2) если x >= 5
# y = x^3 * (a + b) если x < 5


def input_correct(name):
    try:
        n = int(input(f'Введите {name}: '))
    except ValueError:
        print('Надо ввести целое число, внимательнее')
        return input_correct(name)
    else:
        return n


def main():  # основная функция
    try:
        a = input_correct('A')
        b = input_correct('B')
        x = input_correct('X')
        if x >= 5:
            if a + b == 0:
                print('на 0 делить нельзя')
                exit(0)
            y = (5 * x ** 2) / 6 * (a + b) ** 2
        else:
            y = x ** 3 * (a + b)
        print("y = %.1f" % y)
    except ValueError:
        print('Вы не то пишете')


if __name__ == '__main__':
    main()  # вызов основной функции