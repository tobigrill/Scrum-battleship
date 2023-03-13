from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag, QPalette, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
import sys


class GuessButton(QPushButton):
    def __init__(self, row, col):
        super().__init__()
        self.row = row
        self.col = col
        self.setFixedSize(30, 30)
        self.setStyleSheet("background-color: blue")

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.click()

    def click(self):
        self.setEnabled(False)
      
        self.setStyleSheet("background-color: white")

class PlayField(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        for row in range(10):
            row_layout = QHBoxLayout()
            row_layout.setContentsMargins(0, 0, 0, 0)
            row_layout.setSpacing(0)
            for col in range(10):
                button = GuessButton(row, col)
                row_layout.addWidget(button)
            self.layout.addLayout(row_layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Battleship Game")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QHBoxLayout(central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.play_field = PlayField()
       # self.ship_field = ShipField()
        self.layout.addWidget(self.play_field)
      #  self.layout.addWidget(self.ship_field)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
if __name__ == '__main__':
    main()