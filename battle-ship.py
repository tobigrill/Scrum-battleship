"""
starting page, just a code that runs
later the complete code
by tobias
21.03.2023
"""
import sys
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class Battleship(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Battleship")
        self.setGeometry(250, 125, 850, 500)

        #create Label
        starting_label = QLabel(self)
        starting_label.setText("Welcome to Battleship!")
        font = QFont()
        font.setBold(True)
        font.setPointSize(30)
        starting_label.setFont(font)
        starting_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        starting_label.setGeometry(100, 0, 675, 50)

        #import picture
        #image_label = QLabel(self)
        #pixmap = QPixmap("battleshipGIF.gif")
        #image_label.setPixmap(pixmap)
        #image_label.setGeometry(0, 0, 0, 0)

#execute programm
app = QApplication(sys.argv)
window = Battleship()
window.show()
app.exec()
