import hashlib
import sys

from PyQt6.QtWidgets import QListWidgetItem, QDialog, QGridLayout, QLineEdit, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QApplication
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi
import sys



class WelcomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BattleShip")

        # Zentrales Widget erstellen
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout erstellen
        layout = QGridLayout()

        # Button erstellen
        login_button = QPushButton("START")
        login_button.setObjectName("START")
        login_button.clicked.connect(self.show_login_window)

        # Layout anpassen
        layout.addWidget(login_button, 0, 1, 2, 1, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
        central_widget.setLayout(layout)

        # Stylesheet anwenden mit Hintergrundbild
        self.setStyleSheet("""
            QMainWindow {
                background-image: url("Start.jpg");
                background-repeat: no-repeat;
                background-position: center;
                background-size: cover;
                background-attachment: fixed;
            }
           #START {
                background-color: #CCCCCC;
                border: 2px solid #999999;
                color: #333333;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 24px;
                font-weight: bold;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                transition: all 0.3s ease-in-out;
                box-shadow: 2px 2px 2px #999999;
            }
            #START:hover {
                background-color: #999999;
                border-color: #666666;
                color: white;
                box-shadow: none;
                transform: translate(2px, 2px);
            }
          
            """)

        # Fenstergröße einstellen
        self.setGeometry(0, 0, 1000, 750)
        self.center()

    def center(self):
        # Bildschirmgröße ermitteln
        available_geometry = QApplication.primaryScreen().availableGeometry()

        # Widgetgröße ermitteln
        widget_geometry = self.frameGeometry()

        # Widget zentrieren
        widget_geometry.moveCenter(available_geometry.center())
        self.move(widget_geometry.topLeft())

    def show_login_window(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()



class LoginWindow(QDialog):
    users = {}
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi("login.ui",self)
        

        # Buttons erstellen

        self.login_button.clicked.connect(self.login)
        
        self.cancel_button.clicked.connect(self.close)
        
        self.create_button.clicked.connect(self.create_user_window)

  

        
        

    def authenticate(self, username, password):
        if username in self.users:
            hashed_password = self.users[username]
            if hashed_password == hashlib.sha256(password.encode()).hexdigest():
                return True
        

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Überprüfe, ob die Anmeldedaten korrekt sind
        if self.authenticate(username, password):
            print("Erfolgreich eingeloggt!")
            self.lobby_gui = MatchmakingWindow()
            self.lobby_gui.show()
           
        else:
            print("Falscher Benutzername oder Passwort.")
    
    def create_user_window(self):
       
        self.hide()

    # Load create user window UI
        
        create_user = loadUi("create_user.ui", self)

    # Connect buttons
        self.create_button.clicked.connect(self.create_user)
        self.cancel_button.clicked.connect(self.close)
        create_user.show()

    def create_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        password_repeat = self.password_repeat_input.text()

        # Überprüfe, ob alle Felder ausgefüllt sind
        if not username or not password or not password_repeat:
            print("Bitte füllen Sie alle Felder aus.")
            return

        # Überprüfe, ob das Passwort richtig wiederholt wurde
        if password != password_repeat:
            print("Die Passwörter stimmen nicht überein.")
            return

        # Überprüfe, ob der Benutzer bereits existiert
        if username in self.users:
            print("Dieser Benutzername existiert bereits.")
            return

        # Füge den neuen Benutzer hinzu
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.users[username] = hashed_password


        # Öffne das Login-Fenster
        self.login_window = LoginWindow()
        if not self.login_window:
            self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
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


        

        








if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = WelcomeWindow()
    login_window.show()
    sys.exit(app.exec())
