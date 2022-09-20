#!/usr/bin/env python3
# coding=utf-8

import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('Работа с визуальными табличными данными в Python')
        self.setWindowIcon(QtGui.QIcon('images/cat.png'))

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):
        """
        заполняем таблицу случайными числами
        :return:
        """
        row = 0
        col = 0

        # заполняем таблицу случайными числами
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(0, 101)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                col += 1
            row += 1
            col = 0

        self.btn_solve.setEnabled(True)

    def solve(self):
        # -*- решение задания -*-
        row = 0
        col = 0

        zeros_count = 0  # количество 0

        try:

            while row < self.tableWidget.rowCount():
                while col < self.tableWidget.columnCount():
                    item = self.tableWidget.item(row, col).text()
                    if float(item) == 0:
                        zeros_count += 1
                    col += 1

                row += 1
                col = 0

            row = 0

            while row < self.tableWidget.rowCount():
                while col < self.tableWidget.columnCount():
                    item = self.tableWidget.item(row, col).text()
                    if float(item) % 2:
                        self.tableWidget.setItem(row, col, QTableWidgetItem(str(zeros_count)))
                    col += 1

                row += 1
                col = 0

        except:
            self.label_error.setText('Введены неверные значения!')

        else:
            self.label_zeros_count.setText(f'Количество нулей: {zeros_count}')


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
