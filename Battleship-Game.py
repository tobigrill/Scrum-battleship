'''
David Wuerfl
25.04.2023
Battleship-Ship-Placement
'''


import sys
import random
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class In_Game_UI(QWidget):
    
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        button_size = QSize(70, 70)
        button_margin = 0
        
        
        for i in range(1, 11):
            label = QLabel(str(i))
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            grid.addWidget(label, i, 0, 1, 1)
        for j, letter in enumerate(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J" " ", " ", " ", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]):
            label = QLabel(letter)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            grid.addWidget(label, 0, j+1, 1, 1)

        for i in range(1, 11):
            for j in range(10):
                button = QPushButton()
                button.setFixedSize(button_size)
                button.setContentsMargins(button_margin, button_margin, button_margin, button_margin)
                button.setStyleSheet("QPushButton {background-color:#ccf2ff ; color: white; border: 0.5px solid black;}"
                                   "QPushButton:hover {background-color:#cce6ff  ;}")
                grid.addWidget(button, i, j+1)

        for i in range(1, 11):
            for j in range(1):
                spacer = QWidget()
                spacer.setFixedSize(5, 5)
                grid.addWidget(spacer, i, j)

        for i in range(1, 11):
            for j in range(10):
                button = QPushButton()
                button.setFixedSize(button_size)
                button.setContentsMargins(button_margin, button_margin, button_margin, button_margin)
                button.setEnabled(False)
                button.setStyleSheet("QPushButton {background-color:#ccf2ff ; color: white; border: 0.5px solid black;}"
                                   "QPushButton:hover {background-color:#cce6ff  ;}")
                grid.addWidget(button, i, j+14)

        for i in range(1, 11):
            label = QLabel(str(i))
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            grid.addWidget(label, i, 25, 1, 1)
        
        
        buttonQ = QPushButton("X")
        buttonQ.setStyleSheet("QPushButton {background-color: red; color: white; border: 2px solid black;}"
                                   "QPushButton:hover {background-color: #cc0000;}")
        buttonQ.setFixedSize(QSize(20, 20))
        buttonQ.clicked.connect(self.close)
        grid.addWidget(buttonQ, 0,25)
        
        
        
        ships_label = QLabel("Ships Left")
        ships_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(ships_label, 13, 5, 1, 6)
        
        
        
        grid.setColumnMinimumWidth(0, 50)
        grid.setRowMinimumHeight(60, 100)
        grid.setHorizontalSpacing(0)
        grid.setVerticalSpacing(0)
        
        self.setLayout(grid)
        self.setWindowTitle("In a Battle")
        self.showFullScreen()
        self.show()

        
class MainWindow(QWidget):
    

    
    def __init__(self):
        super().__init__()
        self.ship_num = 2
        self.selected_ship = None
        self.ship_size = None
        self.setWindowTitle("Place your Ships")
        self.showFullScreen()

     
        
        self.ship_counts = {
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0
        }
        
        
        self.button_size = QSize(70, 70)
        button_margin = 0

        self.grid_layout = QGridLayout()
        self.radioButton1 = QRadioButton("Patrol Boat")
        self.radioButton1.toggled.connect(lambda checked, size=2: self.set_ship_size(size))
        self.radioButton2 = QRadioButton("Submarine")
        self.radioButton2.toggled.connect(lambda checked, size=3: self.set_ship_size(size))
        self.radioButton3 = QRadioButton("Destroyer")
        self.radioButton3.toggled.connect(lambda checked, size=4: self.set_ship_size(size))
        self.radioButton4 = QRadioButton("Carrier")
        self.radioButton4.toggled.connect(lambda checked, size=5: self.set_ship_size(size))
        self.vertical_checkbox = QCheckBox("Vertical")
        self.buttonC = QPushButton("Confirm")
        self.buttonC.setEnabled(False)
        self.buttonC.setFixedSize(QSize(150, 20))
        self.buttonC.clicked.connect(self.confirm_placement)
        self.buttonQ = QPushButton("X")
        self.buttonQ.setStyleSheet("QPushButton {background-color: red; color: white; border: 2px solid black;}"
                                   "QPushButton:hover {background-color: #cc0000;}")
        self.buttonQ.setFixedSize(QSize(20, 20))
        self.buttonQ.clicked.connect(self.close)
        self.buttonR = QPushButton("Reset")
        self.buttonR.setFixedSize(QSize(150, 20))
        self.buttonR.setStyleSheet("QPushButton {background-color: #c0c0c0; color: black; border: 2px solid black;}"
                                   "QPushButton:hover {background-color:#999999 ;}")
        
        self.buttonR.clicked.connect(self.reset_game)
        self.grid_layout.addWidget(self.buttonQ, 0,15)
        self.grid_layout.addWidget(self.vertical_checkbox, 1,13)
        self.grid_layout.addWidget(self.radioButton1, 2,13)
        self.grid_layout.addWidget(self.radioButton2, 3,13)
        self.grid_layout.addWidget(self.radioButton3, 4,13)
        self.grid_layout.addWidget(self.radioButton4, 5,13)
        self.grid_layout.addWidget(self.buttonC, 6,13)
        self.grid_layout.addWidget(self.buttonR,0,13)
        self.ships = []
        
        self.grid_layout.setVerticalSpacing(0)
        self.grid_layout.setHorizontalSpacing(0)
        self.grid_layout.setSpacing(0)
        self.button_fields = []
        
        
        
        for i in range(10):
            row = []
        
            for j in range(10):
                button = QPushButton()
                button.setObjectName(f"{i},{j}")
                button.setFixedSize(self.button_size)
                button.setContentsMargins(0, 0, 0, 0)
                
                button.setStyleSheet("QPushButton {background-color:#ccf2ff ; color: white; border: 0.5px solid black;}"
                                   "QPushButton:hover {background-color:#cce6ff  ;}")
                self.grid_layout.addWidget(button, i+1, j+1)
                row.append(button)
            self.button_fields.append(row)
        for i in range(10):
            for j in range(10):
                button = self.button_fields[i][j]
                button.clicked.connect(lambda _, x=i, y=j: self.place_ship(x, y))
                
        for i in range(1, 11):
            label = QLabel(str(i))
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.grid_layout.addWidget(label, i, 0, 1, 1)
        for j, letter in enumerate(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]):
            label = QLabel(letter)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.grid_layout.addWidget(label, 0, j+1, 1, 1)
        spacer = QSpacerItem(70, 40)
        self.grid_layout.addItem(spacer, 10+1, 2, 2, 10) 
        self.setLayout(self.grid_layout)
        
        
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
        self.update_confirm_button()
        
    def check_valid_placement(self, x, y, orientation):
        endpoints = self.find_possible_endpoints(x, y, orientation)
        if not endpoints:
            return False
        for endpoint in endpoints:
            if endpoint[0] < 0 or endpoint[0] >= 10 or endpoint[1] < 0 or endpoint[1] >= 10:
                return False
            if self.button_fields[endpoint[0]][endpoint[1]].property("occupied"):
                return False
        x_values = [point[0] for point in endpoints]
        y_values = [point[1] for point in endpoints]
        if min(x_values) < 0 or max(x_values) >= 10 or min(y_values) < 0 or max(y_values) >= 10:
            return False
        return True

    
    
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
                self.ship_num = self.ship_counts[self.selected_ship] + 1
                self.ships.append((self.selected_ship, self.find_possible_endpoints(x, y, "down")))
                for i, j in self.find_possible_endpoints(x, y, "down"):
                    self.button_fields[i][j].setProperty("occupied", True)
                self.ship_counts[self.selected_ship] += 1
                if all(count == 2 for count in self.ship_counts.values()):
                    QMessageBox.information(self, "All ships placed", "All ships have been placed!")
        else:
            if self.check_valid_placement(x, y, "right"):
                self.occupy_cells(x, y, "right")
                self.ship_num = self.ship_counts[self.selected_ship] + 1
                self.ships.append((self.selected_ship, self.find_possible_endpoints(x, y, "right")))
                for i, j in self.find_possible_endpoints(x, y, "right"):
                    self.button_fields[i][j].setProperty("occupied", True)
                self.ship_counts[self.selected_ship] += 1
                if all(count == 2 for count in self.ship_counts.values()):
                    QMessageBox.information(self, "All ships placed", "All ships have been placed!")
        self.update_confirm_button()
        self.id = int(str(self.ship_num) + str(self.selected_ship))
        print(self.id)
    def occupy_cells(self, x, y, orientation):
        endpoints = self.find_possible_endpoints(x, y, orientation)
        for endpoint in endpoints:
            button = self.button_fields[endpoint[0]][endpoint[1]]
            button.setProperty("occupied", True)
            button.setStyleSheet("background-color: #66b3ff; border: 1px solid black")
            button.setText(str(self.ship_num) + str(self.selected_ship))
            button.setEnabled(False)



        
    def find_possible_endpoints(self, x, y, orientation):
        endpoints = []
        if orientation == "right":
            if y + self.ship_size <= 10:
                for j in range(y, y + self.ship_size):
                    endpoints.append((x, j))
        elif orientation == "down":
            if x + self.ship_size <= 10:
                for i in range(x, x + self.ship_size):
                    endpoints.append((i, y))
        return endpoints
    
    def reset_game(self):
        self.ship_counts = {"2": 0, "3": 0, "4": 0, "5": 0}
        self.ships = []
        for i in range(10):
            for j in range(10):
                button = self.button_fields[i][j]
                button.setProperty("occupied", False)
                button.setStyleSheet("QPushButton {background-color:#ccf2ff ; color: white; border: 0.5px solid black;}"
                                   "QPushButton:hover {background-color:#cce6ff  ;}")
                button.setText("")
                button.setEnabled(True)
        self.radioButton1.setEnabled(True)
        self.radioButton2.setEnabled(True)
        self.radioButton3.setEnabled(True)
        self.radioButton4.setEnabled(True)
    
    def update_confirm_button(self):
        if self.ship_counts["2"] == 2 and self.ship_counts["3"] == 2 \
                and self.ship_counts["4"] == 2 and self.ship_counts["5"] == 2:
            self.buttonC.setStyleSheet("QPushButton {background-color: #00cc00; color: black; border: 2px solid black;}"
                                   "QPushButton:hover {background-color:#009900 ;}")
            self.buttonC.setEnabled(True)
            
        else:
            self.buttonC.setEnabled(False)

    def confirm_placement(self):
        reply = QMessageBox.question(self, "Confirm Placement", 
            "Are you ready to play?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.In_Game()


    
    def In_Game(self):
        print(self.button_fields)
        self.close()
        self.window2=In_Game_UI()
        self.window2.show()
    
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())


