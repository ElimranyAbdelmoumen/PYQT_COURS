import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

app = QApplication(sys.argv)
window = QWidget()

layout = QGridLayout()

btn1 = QPushButton('Button 1')
btn2 = QPushButton('Button 2')
btn3 = QPushButton('Button 3')
btn4 = QPushButton('Button 4')
btn5 = QPushButton('Button 5')
btn6 = QPushButton('Button 6')
btns = [btn1,btn2,btn3,btn4,btn5,btn6]

for btn in btns :
    btn.setFixedSize(70,50)

layout.addWidget(btn1,0,0)
layout.addWidget(btn2,0,1)
layout.addWidget(btn3,0,2)
layout.addWidget(btn4,1,0)
layout.addWidget(btn5,1,1)
layout.addWidget(btn6,1,2)

window.setLayout(layout)
window.setWindowTitle('PyQt5 QGridLayout')
window.show()

sys.exit(app.exec_())