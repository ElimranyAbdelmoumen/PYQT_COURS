from PyQt5.QtWidgets import QApplication, QScrollBar, QWidget

app = QApplication([])
window = QWidget()
window.setGeometry(100,100,500,400)
scrollbar = QScrollBar(window)
window.show()
app.exec_()