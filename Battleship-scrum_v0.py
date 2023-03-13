import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QMessageBox, QPushButton, QVBoxLayout, QWidget

import random

class BattleshipGame:
    def __init__(self):
        self.board = [[0] * 5 for _ in range(5)]
        self.ships = [(2, 0, 0, "H"), (3, 3, 1, "V"), (3, 1, 3, "H"), (4, 0, 4, "V")]

        for ship in self.ships:
            size, row, col, orientation = ship
            if orientation == "H":
                for i in range(size):
                    if row >= len(self.board) or col+i >= len(self.board[row]):
                        return
                    self.board[row][col+i] = 1
            else:
                for i in range(size):
                    if row+i >= len(self.board) or col >= len(self.board[row+i]):
                        return
                    self.board[row+i][col] = 1

    def shoot(self, row, col):
        if self.board[row][col] == 1:
            self.board[row][col] = 2
            return True
        else:
            return False

    def is_game_over(self):
        return all(all(cell != 1 for cell in row) for row in self.board)

class BattleshipUI(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the game and the grid layout
        self.game = BattleshipGame()
        self.grid = QGridLayout()

        # Add the labels for the rows and columns
        rows = ["A", "B", "C", "D", "E"]
        cols = ["1", "2", "3", "4", "5"]
        for i in range(len(rows)):
            self.grid.addWidget(QLabel(rows[i]), i+1, 0)
        for i in range(len(cols)):
            self.grid.addWidget(QLabel(cols[i]), 0, i+1)

        # Add the buttons for each cell in the grid
        for i in range(len(rows)):
            for j in range(len(cols)):
                button = QPushButton()
                button.setFixedSize(50, 50)
                button.clicked.connect(lambda _, r=i, c=j: self.cell_clicked(r, c))
                self.grid.addWidget(button, i+1, j+1)

        # Add a layout to center the grid
        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addLayout(self.grid)
        vbox.addStretch()
        self.setLayout(vbox)

        self.setWindowTitle("Battleship")

    def cell_clicked(self, row, col):
        if self.game.shoot(row, col):
            self.grid.itemAtPosition(row+1, col+1).widget().setStyleSheet("background-color: red")
            if self.game.is_game_over():
                self.show_game_over_dialog()
        else:
            self.grid.itemAtPosition(row+1, col+1).widget().setStyleSheet("background-color: gray")

    def show_game_over_dialog(self):
        msg_box = QMessageBox()
        msg_box.setText("Congratulations, you won!")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)

        msg_box.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = BattleshipUI()
    ui.show()
    sys.exit(app.exec())

