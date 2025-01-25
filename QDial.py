from PyQt5.QtWidgets import QApplication, QDial, QWidget

app = QApplication([])
window = QWidget()
dial = QDial(window)
window.show()
app.exec_()