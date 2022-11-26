#!/usr/bin/env python3
# coding=utf-8

# Имеется таблица в два столбца и 10 строк. В первом столбце исходные данные,
# во втором нужно выполнить расчет значений по формуле:
# y = sqrt(Cos(K(i))^2/(a^2-b^2)-Sin(K(i)))*Sum(K(i-1))
# Вычисления произвести используя классы.

import math  # для вычислений


class Aggregate(object):  # объявляем класс
    # Аргумент self обязателен для всех методов всех классов
    def __init__(self):  # конструктор класса
        self.values = []  # инициализируем массив

    def add_value(self, value):  # метод добавления чисел
        self.values.append(value)

    def get_value(self, index):  # геттер
        return self.values[index]

    def multiply(self, index):  # метод подсчета произведений
        prod = 1
        for i in range(index):
            prod *= self.values[i]
        return prod

    def addition(self, index):  # метод посчета сумм
        summa = 0
        if index >= 0:
            for i in range(index):
                summa += self.values[i]
        return summa

    def solution(self, i, a, b):  # метод для решения основного задания
        cos_k_quad = (math.cos(int(self.values[i])) ** 2)
        sum_quad_a_b = (a ** 2 + b ** 2)
        sin_k = math.sin(int(self.values[i]))
        return math.sqrt(cos_k_quad / sum_quad_a_b - sin_k) * self.addition(i - 1)
