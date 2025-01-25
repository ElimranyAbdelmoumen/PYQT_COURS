from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QSpinBox, QHBoxLayout, QLabel
from PyQt5.QtGui import QIcon
import sys

class Fenetre(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Exemple de SpinBox")
        self.setGeometry(500, 200, 500, 400)
        self.setWindowIcon(QIcon('logo.png'))  # Correction du nom de fichier

        self.create_spin()

    def create_spin(self):
        hbox = QHBoxLayout()

        label = QLabel("Prix d'un MacBook :")  # Correction de l'orthographe de "MacBook"

        self.entree = QLineEdit()
        self.sortie = QLineEdit()
        self.sortie.setReadOnly(True)  # Rendre le champ de sortie en lecture seule

        self.spinbox = QSpinBox()
        self.spinbox.valueChanged.connect(self.up_date_values)  # Connecter après la création du spinbox

        hbox.addWidget(label)
        hbox.addWidget(self.entree)
        hbox.addWidget(self.spinbox)
        hbox.addWidget(self.sortie)

        self.setLayout(hbox)

    def up_date_values(self):
        if self.entree.text():  # Vérifier si le champ n'est pas vide
            try:
                prix = int(self.entree.text())
                totalPrix = prix * self.spinbox.value()
                self.sortie.setText(str(totalPrix))
            except ValueError:
                print("Valeur erronée")  # Correction de l'orthographe de "Erronée"
        else:
            print("Merci d'entrer une valeur valide de prix")

app = QApplication(sys.argv)
fen = Fenetre()
fen.show()
app.exec_()