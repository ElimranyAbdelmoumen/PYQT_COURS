from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QCheckBox, QPushButton, QLabel
from PyQt5.QtGui import *

import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My app")
        self.setWindowIcon(QIcon("logo.png"))
        self.setGeometry(500,200,500,400)
        self.create_widgets()

    def create_widgets(self):
        btn = QPushButton("Cliquer ici",self )
        btn.setGeometry(100,100,100,100)

        label = QLabel("valider votre infos",self)
        label.move(100,220)
        label.setStyleSheet("color:green")
        label.setFont(QFont("Times New Roman",15))


app = QApplication(sys.argv)
window = Window()
window.show()

app.exec_()