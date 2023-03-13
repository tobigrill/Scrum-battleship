import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class LoginWindow(QMainWindow):
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
        self.create_button.clicked.connect()

        # Layout anpassen
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.create_button)
        layout.addWidget(self.cancel_button)

        central_widget.setLayout(layout)

        # Benutzerdaten
        self.users = {"admin": "123"}

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Überprüfe, ob die Anmeldedaten korrekt sind
        if username in self.users and self.users[username] == password:
            print("Erfolgreich eingeloggt!")
            self.close()
        else:
            print("Falscher Benutzername oder Passwort.")







if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
