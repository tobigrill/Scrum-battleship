import hashlib
import sys
import socket

HEADER = 64 #first message do the server must be bytes 64 
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"
SERVER = "10.10.209.164"
ADDR =(SERVER, PORT)
usernamesend = "user"
login = "log"
clientError = "wrongPW_BN"
clientwidgetchange = "matchmaking"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QListWidget, QListWidgetItem

class LoginWindow(QMainWindow):
    users = {}
    def __init__(self):
        
        super().__init__()

        self.setWindowTitle("Login")

        # Zentrales Widget erstellen
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout erstellen
        layout = QVBoxLayout()

        # Labels und Eingabefelder erstellen
        self.username_label = QLabel("Benutzername:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Passwort:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Buttons erstellen
        self.login_button = QPushButton("Einloggen")
        self.login_button.clicked.connect(self.login)
        self.cancel_button = QPushButton("Abbrechen")
        self.cancel_button.clicked.connect(self.close)
        self.create_button = QPushButton("Neuen Benutzer erstellen")
        self.create_button.clicked.connect(self.create_user_window)
        
        self.disbutton = QPushButton("disconnect")
        self.disbutton.setCheckable(True)
        self.disbutton.clicked.connect(self.disc)

        # Layout anpassen
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.create_button)
        layout.addWidget(self.cancel_button)
        
        layout.addWidget(self.disbutton)

        central_widget.setLayout(layout)

        # Benutzerdaten
        

    def authenticate(self, username, password):
        if username in self.users:
            hashed_password = self.users[username]
            if hashed_password == hashlib.sha256(password.encode()).hexdigest():
                return True
        

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        send(login)
        send(username)
        hash_password = hashlib.sha256(password.encode()).hexdigest()
        send(hash_password)
        
        widgetchange = client.recv(2048).decode(FORMAT)
        print(widgetchange)
        
        if widgetchange == clientwidgetchange:
            self.close()
            self.matchmaking = MatchmakingWindow()
            self.matchmaking.show()
            
        elif widgetchange == clientError:
            QMessageBox.critical(self,"Error","password or username are wrong")
            


    def create_user_window(self):
        self.setWindowTitle("Neuen Benutzer erstellen")

        # Zentrales Widget erstellen
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout erstellen
        layout = QVBoxLayout()

        # Labels und Eingabefelder erstellen
        self.username_label = QLabel("Benutzername:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Passwort:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_repeat_label = QLabel("Passwort wiederholen:")
        self.password_repeat_input = QLineEdit()
        self.password_repeat_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Buttons erstellen
        self.create_button = QPushButton("Benutzer erstellen")
        self.create_button.clicked.connect(self.create_user)
        self.cancel_button = QPushButton("Abbrechen")
        self.cancel_button.clicked.connect(self.close)

        # Layout anpassen
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.password_repeat_label)
        layout.addWidget(self.password_repeat_input)
        layout.addWidget(self.create_button)
        layout.addWidget(self.cancel_button)

        central_widget.setLayout(layout)

        # Benutzerdaten
        

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
        send(usernamesend)
        send(username)
        send(hashed_password)
        

        # Öffne das Login-Fenster
        self.login_window = LoginWindow()
        if not self.login_window:
            self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
        
    def disc(self):
        send(DISCONNECT_MESSAGE)   
        sys.exit()
        
        
class MatchmakingWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Matchmaking")


        self.find_match_button = QPushButton("Spiel suchen")
        self.players_label = QLabel("Online Spieler:")
        self.players_list_widget = QListWidget()
        
        self.disbutton = QPushButton("disconnect")
        self.disbutton.setCheckable(True)
        self.disbutton.clicked.connect(self.disco)


        button_layout = QHBoxLayout()
        button_layout.addWidget(self.find_match_button)
        button_layout.addWidget(self.disbutton)
        
        players_layout = QVBoxLayout()
        players_layout.addWidget(self.players_label)
        players_layout.addWidget(self.players_list_widget)

        main_layout = QVBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addLayout(players_layout)

        self.setLayout(main_layout)

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
        
    def disco(self):
        send(DISCONNECT_MESSAGE)   
        sys.exit()

        
def send(msg):
    message = msg.encode(FORMAT)
    msg_length= len(message)
    send_length = str(msg_length).encode(FORMAT)                   
    send_length += b' '* (HEADER-len(send_length))
    
    client.send(send_length)
    client.send(message)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())