from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CheckBox")
        self.setGeometry(500,200,500,400)
        self.data = "-"
    
        self.create_box()

    def create_box(self):
        hbox = QHBoxLayout()

        self.check1 = QCheckBox("Python")
        hbox.addWidget(self.check1)

        self.check2 = QCheckBox("C++")
        hbox.addWidget(self.check2)

        self.check3 = QCheckBox("Java")
        hbox.addWidget(self.check3)

        self.check4 = QCheckBox("C")
        hbox.addWidget(self.check4)
        self.label = QLabel("Bonjour <" + self.data + ">")
        vbox =QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.check1.toggled.connect(self.upDate)
        self.check2.toggled.connect(self.upDate)
        self.check3.toggled.connect(self.upDate)
        self.check4.toggled.connect(self.upDate)
        
    def upDate(self):
        self.data = " "
        if self.check1.isChecked():
            self.data += self.check1.text()
        if self.check2.isChecked():
            self.data += ", " + self.check2.text()
        if self.check3.isChecked():
            self.data += ", " + self.check3.text()
        if self.check4.isChecked():
            self.data += ", " + self.check4.text()

        self.label.setText("Bonjour <" + self.data + ">")

             
    
        
app = QApplication(sys.argv)
fen = Window()
fen.show()
app.exec_()