'''
David Wuerfl
19.03.2023
Battleship-Ship-Placement
'''


import sys
import random
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.selected_ship = None
        self.ship_size = None
        self.setWindowTitle("Battleship-test")
        self.setFixedSize(QSize(700, 680))

        self.menu = self.menuBar()
        self.options_menu = self.menu.addMenu("Options")

        self.quit_action = QAction("Quit", self)
        self.quit_action.triggered.connect(QApplication.instance().quit)
        self.options_menu.addAction(self.quit_action)
        
        self.ship_counts = {
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0
        }
        
        self.size = 10
        self.sizeb = 10
        self.button_size = 50
        self.button_sizeb = 70

        self.options_layout = QVBoxLayout()
        self.radioButton1 = QRadioButton("Patrol Boat")
        self.radioButton1.toggled.connect(lambda checked, size=2: self.set_ship_size(size))
        self.radioButton2 = QRadioButton("Submarine")
        self.radioButton2.toggled.connect(lambda checked, size=3: self.set_ship_size(size))
        self.radioButton3 = QRadioButton("Destroyer")
        self.radioButton3.toggled.connect(lambda checked, size=4: self.set_ship_size(size))
        self.radioButton4 = QRadioButton("Carrier")
        self.radioButton4.toggled.connect(lambda checked, size=5: self.set_ship_size(size))
        self.vertical_checkbox = QCheckBox("Vertical")
        
        self.options_layout.addWidget(self.vertical_checkbox)
        self.options_layout.addWidget(self.radioButton1)
        self.options_layout.addWidget(self.radioButton2)
        self.options_layout.addWidget(self.radioButton3)
        self.options_layout.addWidget(self.radioButton4)
        
        self.options_frame = QFrame()
        self.options_frame.setLayout(self.options_layout)
        self.options_dock = QDockWidget("Ships", self)
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
        for i in range(self.size):
            for j in range(self.size):
                button = self.button_fields[i][j]
                button.clicked.connect(lambda _, x=i, y=j: self.place_ship(x, y))

        self.field_widget = QWidget()
        self.field_widget.setLayout(self.grid_layout)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.field_widget)
        self.setCentralWidget(self.scroll_area)
        
    def set_ship_size(self, size=2):
        self.ship_size = size
        if size == 2:
            self.selected_ship = "2"
        elif size == 3:
            self.selected_ship = "3"
        elif size == 4:
            self.selected_ship = "4"
        elif size == 5:
            self.selected_ship = "5"
        if self.ship_counts[self.selected_ship] >= 2:
            if size == 2:
                self.radioButton1.setEnabled(False)
            elif size == 3:
                self.radioButton2.setEnabled(False)
            elif size == 4:
                self.radioButton3.setEnabled(False)
            elif size == 5:
                self.radioButton4.setEnabled(False)
    
    def check_valid_placement(self, x, y, orientation):
        endpoints = self.find_possible_endpoints(x, y, orientation)
        if not endpoints:
            return False
        for endpoint in endpoints:
            if endpoint[0] < 0 or endpoint[0] >= self.size or endpoint[1] < 0 or endpoint[1] >= self.size:
                return False
            if self.button_fields[endpoint[0]][endpoint[1]].property("occupied"):
                return False
        x_values = [point[0] for point in endpoints]
        y_values = [point[1] for point in endpoints]
        if min(x_values) < 0 or max(x_values) >= self.size or min(y_values) < 0 or max(y_values) >= self.size:
            return False
        return True

    def occupy_cells(self, x, y, orientation):
        endpoints = self.find_possible_endpoints(x, y, orientation)
        for endpoint in endpoints:
            button = self.button_fields[endpoint[0]][endpoint[1]]
            button.setProperty("occupied", True)
            button.setStyleSheet("background-color: #66b3ff")
            button.setText(self.selected_ship)
            button.setEnabled(False)
    
    def place_ship(self, x, y):
        if self.selected_ship is None:
            QMessageBox.warning(self, "No ship selected", "Please select a ship first.")
            return
        if self.ship_counts[self.selected_ship] >= 2:
            QMessageBox.warning(self, "Ship limit reached", f"You cannot place any more {self.selected_ship} ships.")
            return
        if self.vertical_checkbox.isChecked():
            if self.check_valid_placement(x, y, "down"):
                self.occupy_cells(x, y, "down")
                ship_num = self.ship_counts[self.selected_ship] + 1
                self.ships.append((self.selected_ship, self.find_possible_endpoints(x, y, "down")))
                for i, j in self.find_possible_endpoints(x, y, "down"):
                    self.button_fields[i][j].setProperty("occupied", True)
                self.ship_counts[self.selected_ship] += 1
                if all(count == 2 for count in self.ship_counts.values()):
                    QMessageBox.information(self, "All ships placed", "All ships have been placed!")
        else:
            if self.check_valid_placement(x, y, "right"):
                self.occupy_cells(x, y, "right")
                ship_num = self.ship_counts[self.selected_ship] + 1
                self.ships.append((self.selected_ship, self.find_possible_endpoints(x, y, "right")))
                for i, j in self.find_possible_endpoints(x, y, "right"):
                    self.button_fields[i][j].setProperty("occupied", True)
                self.ship_counts[self.selected_ship] += 1
                if all(count == 2 for count in self.ship_counts.values()):
                    QMessageBox.information(self, "All ships placed", "All ships have been placed!")

    def find_possible_endpoints(self, x, y, orientation):
        endpoints = []
        if orientation == "right":
            if y + self.ship_size <= self.size:
                for j in range(y, y + self.ship_size):
                    endpoints.append((x, j))
        elif orientation == "down":
            if x + self.ship_size <= self.size:
                for i in range(x, x + self.ship_size):
                    endpoints.append((i, y))
        return endpoints
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())