from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QLabel

import sys 

app = QApplication(sys.argv)

window = QTabWidget()
window.setGeometry(100, 100, 400, 300) 

tab1 = QWidget()
tab2 = QWidget()

label1 = QLabel('Contenu de l\'onglet 1', tab1)
label1.move(20, 20)  

label2 = QLabel('Contenu de l\'onglet 2', tab2)
label2.move(20, 20)

window.addTab(tab1, "Onglet 1")
window.addTab(tab2, "Onglet 2")

window.show()

app.exec_()