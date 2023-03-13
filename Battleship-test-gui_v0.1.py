import sys
from PyQt6 import *
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QColor, QPainter, QBrush, QPen
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout


class Grid:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = [[None for y in range(height)] for x in range(width)]

    def draw(self, qp):
        pen = QPen(QColor("black"))
        pen.setWidth(1)
        qp.setPen(pen)
        for x in range(self.width + 1):
            qp.drawLine(x * self.cell_size, 0, x * self.cell_size, self.height * self.cell_size)
        for y in range(self.height + 1):
            qp.drawLine(0, y * self.cell_size, self.width * self.cell_size, y * self.cell_size)

    def get_cell(self, x, y):
        return self.grid[x][y]

    def set_cell(self, x, y, square):
        self.grid[x][y] = square


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('PyQT6 Game')
        self.show()
     
    def drawGrid(self, qp):
        pen = QPen(QColor("black"))
        pen.setWidth(1)
        qp.setPen(pen)
        
        # Draw the vertical and horizontal lines for the grid
        for i in range(11):
            qp.drawLine(i*30, 0, i*30, 300)
            qp.drawLine(0, i*30, 300, i*30)

 



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())