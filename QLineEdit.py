from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget

app = QApplication([])
window = QWidget()
line_edit = QLineEdit(window)
window.show()
app.exec_()