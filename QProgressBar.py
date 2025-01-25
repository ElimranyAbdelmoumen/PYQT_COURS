from PyQt5.QtWidgets import QApplication, QProgressBar, QWidget

app = QApplication([])
window = QWidget()

progress_bar = QProgressBar(window)
progress_bar.setValue(50)

window.show()
app.exec_()