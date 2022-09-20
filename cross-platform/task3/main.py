#!/usr/bin/env python3
# coding=utf-8
'''
ПРИМЕР 2 ДЛЯ ДВУМЕРНОГО МАССИВА
'''
import random

src_array = []
for row in range(1, 10):
    src_array.append([random.randint(-10, 10) for cell in range(1, 10)]
)

zeros_count = 0

for row, r in enumerate(src_array):  # Перебираем строки
    for col, cell in enumerate(r):  # Перебираем столбцы
        print(cell, end=' ')
        if cell == 0:  # Если cчитаем нули
            zeros_count += 1
    print()

for row, r in enumerate(src_array):  # Перебираем строки
    for col, cell in enumerate(r):  # Перебираем столбцы
        if cell % 2 == 1:
            src_array[row][col] = zeros_count #замена нечетных целых на количество нулей

print(f'\nzeros count: {zeros_count}\n')

for b in src_array:  # Вывод массива на экран
    print(b)

print()
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
