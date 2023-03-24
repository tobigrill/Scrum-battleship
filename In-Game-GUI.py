'''
David Würfl
24.03.2023
In-Game GUI
'''

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()

        
        enemy_label = QLabel("Enemy Field")
        enemy_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(enemy_label, 0, 0, 1, 10)

       
        for i in range(1, 11):
            for j in range(10):
                button = QPushButton()
                grid.addWidget(button, i, j)

        
        for i in range(1, 11):
            for j in range(2):
                spacer = QWidget()
                spacer.setFixedSize(10, 10)
                grid.addWidget(spacer, i, j+10)

       
        your_label = QLabel("Your Field")
        your_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(your_label, 0, 12, 1, 10)


        for i in range(1, 11):
            for j in range(10):
                button = QPushButton()
                grid.addWidget(button, i, j+12)

    
        shoot_button = QPushButton("Shoot")
        shoot_button.setFixedSize(100, 50)
        grid.addWidget(shoot_button, 12, 0, 1, 10)

        self.setLayout(grid)
        self.setGeometry(100, 100, 500, 400)
        self.setWindowTitle('Buttonfelder')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Window()
    sys.exit(app.exec())
