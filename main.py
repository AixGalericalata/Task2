import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.draw = False
        self.pushButton.clicked.connect(self.dr)

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            self.paint(qp)
            qp.end()

    def dr(self):
        self.draw = True
        self.repaint()

    def paint(self, qp):
        r = random.randint(10, 100)
        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(self.width() / 2 - r, self.height() / 2 - r, 2 * r, 2 * r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())