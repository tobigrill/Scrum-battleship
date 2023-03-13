import sys
from PyQt6 import *
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QColor, QPainter, QBrush, QPen
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout


class Square:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = QColor(color)

    def draw(self, qp):
        brush = QBrush(self.color)
        pen = QPen(QColor("black"))
        pen.setWidth(2)
        qp.setPen(pen)
        qp.setBrush(brush)
        qp.drawRect(self.x, self.y, self.width, self.height)

    def contains(self, x, y):
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height


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
        self.grid_locked = False
        # Initialize the squares
        
        self.square1 = Square(0, 0, 30, 30, "#FF0000")
        self.square2 = Square(0, 0, 30, 60, "#00FF00")
        self.square3 = Square(0, 0, 30, 90, "#0000FF")
        self.square4 = Square(0, 0, 30, 120, "#FFFF00")
        button_widget = QWidget(self)
        button_widget.setGeometry(310, 0, 290, 300)
        button_layout = QGridLayout(button_widget)
        # Initialize the grabbed square
        self.grabbed_square = None
        for i in range(10):
            for j in range(10):
                button = QPushButton(f"{i},{j}", button_widget)
                button_layout.addWidget(button, i, j)

        self.show()
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawGrid(qp)

        # Draw the squares
        self.square1.draw(qp)
        self.square2.draw(qp)
        self.square3.draw(qp)
        self.square4.draw(qp)

        qp.end()

    def drawGrid(self, qp):
        pen = QPen(QColor("black"))
        pen.setWidth(1)
        qp.setPen(pen)
        
        # Draw the vertical and horizontal lines for the grid
        for i in range(11):
            qp.drawLine(i*30, 0, i*30, 300)
            qp.drawLine(0, i*30, 300, i*30)

    def mousePressEvent(self, event):
     if event.button() == Qt.MouseButton.LeftButton:
        if self.square1.contains(event.pos().x(), event.pos().y()):
            self.grabbed_square = self.square1
        elif self.square2.contains(event.pos().x(), event.pos().y()):
            self.grabbed_square = self.square2
        elif self.square3.contains(event.pos().x(), event.pos().y()):
            self.grabbed_square = self.square3
        elif self.square4.contains(event.pos().x(), event.pos().y()):
            self.grabbed_square = self.square4

     if self.grabbed_square is not None:
        self.grabbed_square.x = event.pos().x() - self.grabbed_square.width // 2
        self.grabbed_square.y = event.pos().y() - self.grabbed_square.height // 2

        self.update()



    def mousePressEvent(self, event):
     if event.button() == Qt.MouseButton.LeftButton:
        if self.square1.contains(event.pos().x(), event.pos().y()):
            self.grabbed_square = self.square1
        elif self.square2.contains(event.pos().x(), event.pos().y()):
            self.grabbed_square = self.square2
        elif self.square3.contains(event.pos().x(), event.pos().y()):
            self.grabbed_square = self.square3
        elif self.square4.contains(event.pos().x(), event.pos().y()):
            self.grabbed_square = self.square4
        else:
            self.grabbed_square = None
     self.update()


    def mouseMoveEvent(self, event):
     if self.grabbed_square is not None:
        new_x = event.pos().x() - self.grabbed_square.width // 2
        new_y = event.pos().y() - self.grabbed_square.height // 2
        # Check if the new position is inside the grid
        if new_x >= 0 and new_x + self.grabbed_square.width <= 300 and new_y >= 0 and new_y + self.grabbed_square.height <= 300:
            # Check if the new position is inside the left 10x10 grid
            if new_x < 300 and new_y < 300:
                self.grabbed_square.x = new_x
                self.grabbed_square.y = new_y
                self.update()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())