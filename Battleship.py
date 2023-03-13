import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Battleship")
        self.setGeometry(100, 100, 220, 200)
        label = QLabel(self)
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        label.setText("This is going to be a multiplayer battleship-game, with drag and drop ship placement and other nice features. Stay tuned for updates!")
        label.setWordWrap(True)
        label.move(50, 10)
        label1.setText("battleship-game, with drag and drop ship placement and other nice features. Stay tuned for updates!")
        label1.setWordWrap(True)
        label1.move(50, 42)
        label2.setText("drop ship placement and other nice features. Stay tuned for updates!")
        label2.setWordWrap(True)
        label2.move(50, 74)
        label3.setText("other nice features.")
        label3.setWordWrap(True)
        label3.move(50, 106)
        label4.setText("Stay tuned for updates!")
        label4.setWordWrap(True)
        label4.move(50, 150)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
