import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
window = QWidget()

# Créer un layout horizontal
layout = QHBoxLayout()

# Créer les boutons et définir leur taille fixe
btn1 = QPushButton('Button one')
btn1.setFixedSize(100, 50)  # Définir la taille fixe pour btn1

btn2 = QPushButton('Button two')
btn2.setFixedSize(100, 50)  # Définir la taille fixe pour btn2

btn3 = QPushButton('Button three')
btn3.setFixedSize(100, 50)  # Définir la taille fixe pour btn3

btn4 = QPushButton('Button four')
btn4.setFixedSize(100, 50)  # Définir la taille fixe pour btn4

# Ajouter les boutons au layout
layout.addWidget(btn1)
layout.addWidget(btn2)
layout.addWidget(btn3)
layout.addWidget(btn4)

# Fonction pour gérer les clics sur les boutons
def On_click_btn():
    button = window.sender()  # Récupère le bouton qui a émis le signal
    alert = QMessageBox()
    alert.setText(f"Vous avez cliqué sur {button.text()}")
    alert.exec()

# Connecter le signal clicked de chaque bouton à la fonction On_click_btn
btn1.clicked.connect(On_click_btn)
btn2.clicked.connect(On_click_btn)
btn3.clicked.connect(On_click_btn)
btn4.clicked.connect(On_click_btn)

# Appliquer le layout à la fenêtre
window.setLayout(layout)
window.setWindowTitle('PyQt5 QHBoxLayout : Boutons de taille fixe')
window.show()

sys.exit(app.exec_())