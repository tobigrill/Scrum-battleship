import hashlib
import sys
import socket

HEADER = 64 #first message do the server must be bytes 64 
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"
SERVER = "192.168.1.7"
ADDR =(SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


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

        # Überprüfe, ob die Anmeldedaten korrekt sind
        if self.authenticate(username, password):
            print("Erfolgreich eingeloggt!")
            self.close()
        else:
            print("Falscher Benutzername oder Passwort.")

    
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
        send(username,hashed_password)

        # Öffne das Login-Fenster
        self.login_window = LoginWindow()
        if not self.login_window:
            self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
        
    def disc(self):
        send(DISCONNECT_MESSAGE)   
        sys.exit()
        
def send(msgbn,msgpw):
    message1 = msgbn.encode(FORMAT)
    message2 = msgpw.encode(FORMAT)
    
    msg_length1= len(message1)
    send_length1 = str(msg_length1).encode(FORMAT)                   
    send_length1 += b' '* (HEADER-len(send_length1))
    
    msg_length2= len(message2)
    send_length2 = str(msg_length2).encode(FORMAT)                   
    send_length2 += b' '* (HEADER-len(send_length2))
    
    client.send(send_length1)
    client.send(message1)
    
    client.send(send_length2)
    client.send(message2)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())