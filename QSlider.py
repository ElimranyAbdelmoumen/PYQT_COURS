from PyQt5.QtWidgets import QApplication, QSlider, QWidget

app = QApplication([])
window = QWidget()
slider = QSlider(window)
window.show()
app.exec_()