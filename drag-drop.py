from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem
from PyQt6.QtGui import QDrag, QMouseEvent, QPixmap, QCursor, QDropEvent, QDragEnterEvent, QDragMoveEvent
from PyQt6.QtCore import Qt, QPointF, QMimeData
import sys

class Ship(QGraphicsPixmapItem):
    def __init__(self, pixmap):
        super().__init__(pixmap)
        self.setAcceptDrops(True)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            drag = QDrag(event.widget())
            mime_data = QMimeData()
            drag.setMimeData(mime_data)
            drag.setPixmap(self.pixmap())
            drag.setHotSpot(event.pos().toPoint())
            drag.exec(Qt.DropAction.MoveAction)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasFormat("image/x-pixmap"):
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event: QDragMoveEvent):
        if event.mimeData().hasFormat("image/x-pixmap"):
            event.setDropAction(Qt.DropAction.MoveAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasFormat("image/x-pixmap"):
            self.setPos(event.scenePos())
            event.setDropAction(Qt.DropAction.MoveAction)
            event.accept()
        else:
            event.ignore()

class BattleShipGame(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        ship = Ship(QPixmap("image.png"))
        self.scene.addItem(ship)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = BattleShipGame()
    game.show()
    sys.exit(app.exec())
