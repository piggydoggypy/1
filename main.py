import sys

from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLCDNumber, QLineEdit, QMainWindow, QButtonGroup
from PyQt6 import uic
import io
from PyQt6.QtGui import QPainter, QColor
from random import randint


class SimplePlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 100, 800, 600)
        self.pushButton = QPushButton('myau', self)
        self.pushButton.move(400, 400)
        self.pushButton.clicked.connect(self.painterest)
        self.pushButton.resize(100, 100)
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
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        painter.setBrush(QColor(r, g, b))

        x = randint(50, 400)
        painter.drawEllipse(randint(0, self.width() - 200), randint(0, self.height() - 200),
                            x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimplePlanner()
    window.show()
    sys.exit(app.exec())
