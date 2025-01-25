from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QSpinBox, QHBoxLayout, QLabel
from PyQt5.QtGui import QIcon
import sys

app = QApplication(sys.argv)

fen = QWidget()
fen.setWindowIcon(QIcon('logo.png'))
fen.setWindowTitle("PyQT SpinBox")
fen.setGeometry(500, 200, 500, 400)

hbox = QHBoxLayout()

entrer = QLineEdit()
sortie = QLineEdit()
spinbox = QSpinBox()
label = QLabel("Prix d'un MacBook :")

def VChanged():
    if entrer.text():
        try:
            prix = int(entrer.text())  # Utiliser entrer.text() au lieu de entrer.text
            finalprix = spinbox.value() * prix
            sortie.setText(str(finalprix))
        except ValueError:
            print("Valeur erronée")
    else:
        print("Merci d'entrer une valeur valide de prix")
spinbox.valueChanged.connect(VChanged)

hbox.addWidget(label)
hbox.addWidget(entrer)
hbox.addWidget(spinbox)
hbox.addWidget(sortie)

fen.setLayout(hbox)
fen.show()
app.exec_()