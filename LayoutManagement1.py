import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

app = QApplication(sys.argv)
window = QWidget()

layout = QVBoxLayout()
btn1 = QPushButton('Button 1')
btn2 = QPushButton('Button 2')
btn3 = QPushButton('Button 3')
btn4 = QPushButton('Button 4')
layout.addWidget(btn1)
layout.addWidget(btn2)
layout.addWidget(btn3)
layout.addWidget(btn4)

window.setLayout(layout)
window.setWindowTitle('PyQt5 QVBoxLayout')
window.show()

sys.exit(app.exec_())