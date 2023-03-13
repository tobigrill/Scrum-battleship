import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QPixmap, QDrag
from PyQt6.QtCore import Qt, QMimeData


class Button(QPushButton):
    def __init__(self, x, y, parent):
        super().__init__(parent)
        self.setFixedSize(30, 30)
        self.x = x
        self.y = y
        self.setStyleSheet("background-color: white; border: 1px solid black")

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        #if self.parent().parent().image_label.pixmap() is not None:
        #if self.x == self.parent().parent().image_x and self.y == self.parent().parent().image_y:
              #  self.setStyleSheet("background-color: red; border: 1px solid black")

    def reset_style(self):
        self.setStyleSheet("background-color: white; border: 1px solid black")

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
class ImageLabel(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(300, 300)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("border: 1px solid black")
        self.setAcceptDrops(True)
        self.pixmap_image = None
        self.parent = parent

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.DropAction.MoveAction)
            event.accept()
            self.pixmap_image = QPixmap(event.mimeData().imageData())
            self.setPixmap(self.pixmap_image)
            self.parent.image_x = 0
            self.parent.image_y = 0

    def mousePressEvent(self, event):
        if self.pixmap_image is not None:
            if event.button() == Qt.MouseButton.LeftButton:
                self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if self.pixmap_image is not None:
            if not (event.buttons() and Qt.MouseButton.LeftButton):
                return
            drag = QDrag(self)
            mime_data = QMimeData()
            mime_data.setImageData(self.pixmap_image)
            drag.setMimeData(mime_data)
            drag.setPixmap(self.pixmap_image.scaled(30, 30))
            drag.setHotSpot(event.pos() - self.drag_start_position)
            drag.exec_(Qt.DropAction.MoveAction)

    def reset_image(self):
        self.pixmap_image = None
        self.clear()
        self.parent.image_x = -1
        self.parent.image_y = -1


class DragDropImage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 640, 360)
        self.setWindowTitle("Drag & Drop Image")
        self.image_label = ImageLabel(self)
        self.image_label.move(330, 30)

        self.image_x = -1
        self.image_y = -1

        for i in range(10):
            for j in range(10):
                button = Button(i, j, self)
                button.move(i * 30 + 10, j * 30 + 10)

        reset_button = QPushButton("Reset", self)
        reset_button.move(330, 330)
        reset_button.clicked.connect(self.reset_all)

        confirm_button = QPushButton("Confirm", self)
        confirm_button.move(470, 330)
        confirm_button.clicked.connect(self.confirm_position)

        self.show()
    
    def reset_all(self):
        for button in self.findChildren(Button):
            button.reset_style()
        self.image_label.reset_image()

    def confirm_position(self):
        if self.image_label.pixmap_image is not None and self.image_x != -1 and self.image_y != -1:
            for button in self.findChildren(Button):
                if button.x == self.image_x and button.y == self.image_y:
                    button.setStyleSheet("background-color: red; border: 1px solid black")
                else:
                    button.reset_style()
'''
    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Quit", "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
'''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    drag_drop_image = DragDropImage()
    sys.exit(app.exec())

