#!/usr/bin/env python3
# coding=utf-8

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа со строками в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)

    def flatten(self, l):
        return [item for sublist in l for item in sublist]

    def split(self, s, size):
        return [s[i:i + size] for i in range(0, len(s), size)]

    def solve(self):
        self.textEdit_dst.clear()
        text = self.textEdit_src.toPlainText()  # получаем наш текст
        paragraphs = text.split("$")
        chunks = [self.split(p, 60) for p in paragraphs]
        for s in self.flatten(chunks):
            self.textEdit_dst.insertPlainText(s+"\n")

    def clear(self):
        self.textEdit_src.clear()
        self.textEdit_dst.clear()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
