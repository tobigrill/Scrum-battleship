from PyQt6.QtWidgets import *
import sys 
import random
from layout_colorwidget import Color



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Client Color Request")
        
        self.pagelayout = QVBoxLayout()
        self.stacklayout = QStackedLayout()

        
        
        
        button = QPushButton("Get Color")
        button.setCheckable(True)
        button.clicked.connect(self.button_was_clicked)
        
        self.pagelayout.addWidget(button)
        self.pagelayout.addLayout(self.stacklayout)
        
        
        self.stacklayout.addWidget(Color("White"))
        
        widget = QWidget()
        widget.setLayout(self.pagelayout)
        self.setCentralWidget(widget)

    def button_was_clicked(self):
        allcolors =["red","black","green","blue","yellow"] 
        clr = random.choice(allcolors)
        print(clr)
        
        self.stacklayout.addWidget(Color(clr))
        widget = QWidget()
        widget.setLayout(self.pagelayout)
        self.setCentralWidget(widget)
        
        self.stacklayout.setCurrentIndex(1)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
