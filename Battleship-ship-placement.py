'''
David Wuerfl
18.03.23
Battleship ship placement
'''

import sys
import random
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    app = QApplication(sys.argv)
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Battleship-test")
        self.setFixedSize(QSize(700, 680)) 

        self.menu = self.menuBar()
        self.options_menu = self.menu.addMenu("Options")

        self.quit_action = QAction("Quit", self)
        self.quit_action.triggered.connect(QApplication.instance().quit)
        self.options_menu.addAction(self.quit_action)
        
        self.size = 10
        self.sizeb = 10
        self.button_size = 50
        self.button_sizeb = 70
    
        self.options_layout = QVBoxLayout()
        
        self.radioButton1 = QRadioButton("Patrol Boat")
        self.radioButton1.toggled.connect(lambda:self.set_ship_size(2))
        self.radioButton2 = QRadioButton("Submarine")
        self.radioButton2.toggled.connect(lambda:self.set_ship_size(3))
        self.radioButton3 = QRadioButton("Destroyer")
        self.radioButton3.toggled.connect(lambda:self.set_ship_size(1))
        self.radioButton4 = QRadioButton("Carrier")
        self.radioButton4.toggled.connect(lambda:self.set_ship_size(4))
        
        self.options_layout.addWidget(self.radioButton1)
        self.options_layout.addWidget(self.radioButton2)
        self.options_layout.addWidget(self.radioButton3)
        self.options_layout.addWidget(self.radioButton4)

        self.options_frame = QFrame()
        self.options_frame.setLayout(self.options_layout)
        self.options_dock = QDockWidget("Options", self)
        self.options_dock.setWidget(self.options_frame)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.options_dock)

        self.ships = []
    
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(0)
        
        self.button_fields = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                button = QPushButton()
                button.setObjectName(f"{i},{j}")
                button.setFixedSize(self.button_size, self.button_size)
                button.setStyleSheet("background-color: #e6f3ff")
                self.grid_layout.addWidget(button, i, j)
                row.append(button)
            self.button_fields.append(row)
    
        self.field_widget = QWidget()
        self.field_widget.setLayout(self.grid_layout)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.field_widget)
        self.setCentralWidget(self.scroll_area)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())