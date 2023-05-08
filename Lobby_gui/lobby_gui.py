import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QListWidget, QListWidgetItem
from PyQt6.uic import loadUi
class MatchmakingWindow(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("lobby_guii.ui",self)
      


        

        # Button-Click-Event hinzufügen
        self.find_match_button.clicked.connect(self.find_match)

        # Spieler hinzufügen
        self.add_player("tobi")                                                        
        self.add_player("David")
        self.add_player("Nick")

    def add_player(self, player_name):
        item = QListWidgetItem(player_name)
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.players_list_widget.addItem(item)

    def find_match(self):
        # TODO: Implementierung des Matchmaking-Algorithmus
        print("Spieler wird angefragt...")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MatchmakingWindow()
    window.show()
    sys.exit(app.exec())
