from PyQt5.QtWidgets import QApplication, QDateTimeEdit, QWidget

app = QApplication([])
window = QWidget()
datetime_edit = QDateTimeEdit(window)
window.show()
app.exec_()