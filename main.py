import sys

from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLCDNumber, QLineEdit, QMainWindow, QButtonGroup
from PyQt6 import uic
import io
from PyQt6.QtGui import QPainter, QColor
from random import randint


class SimplePlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.painterest)
        self.do_draw = False

    def painterest(self):
        self.do_draw = True
        self.update()

    def paintEvent(self, event):
        if self.do_draw:
            self.painter()
        self.do_draw = False

    def painter(self):
        painter = QPainter()
        painter.begin(self)
        self.paint(painter)
        painter.end()

    def paint(self, painter):
        painter.setBrush(QColor(255, 255, 0))
        x = randint(50, 400)
        painter.drawEllipse(randint(0, self.width() - 200), randint(0, self.height() - 200),
                            x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimplePlanner()
    window.show()
    sys.exit(app.exec())
