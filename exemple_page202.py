from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QGridLayout, QButtonGroup
import sys
app = QApplication(sys.argv)

fen = QWidget()
fen.setGeometry(500,200,500,400)
fen.setWindowTitle("My App")
layout = QGridLayout(fen)


radio1 = QRadioButton("Python")
radio2 = QRadioButton("C++")
radio3 = QRadioButton("Java")


button_group = QButtonGroup()
button_group.addButton(radio1)
button_group.addButton(radio2)
button_group.addButton(radio3)

label = QLabel("Bonjour < >")
layout.addWidget(label,1,0)

layout.addWidget(radio1,3,0)
layout.addWidget(radio2,3,1)
layout.addWidget(radio3,3,2)

def update_label():
    selected = button_group.checkedButton()
    if selected:
        label.setText(f"Bonjour , tu as choisi {selected.text()}")
    else:
        label.setText("Bonjour < >")

radio1.toggled.connect(update_label)
radio2.toggled.connect(update_label)
radio3.toggled.connect(update_label)

fen.show()
app.exec_()
