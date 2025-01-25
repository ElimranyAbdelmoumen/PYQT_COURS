from PyQt5.QtWidgets import QApplication, QComboBox, QWidget

app = QApplication([])
window = QWidget()
combo_box = QComboBox(window)
combo_box.addItem('Option 1')
combo_box.addItem('Option 2')
window.show()
app.exec_()