from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QWidget

app = QApplication([])

# Créer la fenêtre principale
window = QWidget()
window.setWindowTitle('Tableau Exemple')

# Créer un tableau avec 3 lignes et 3 colonnes
table = QTableWidget(3, 3, window)
table.setHorizontalHeaderLabels(['Colonne 1', 'Colonne 2', 'Colonne 3'])  # Ajouter des en-têtes de colonnes

# Remplir le tableau avec des éléments
table.setItem(0, 0, QTableWidgetItem('1'))
table.setItem(1, 1, QTableWidgetItem('2'))
table.setItem(2, 2, QTableWidgetItem('3'))


table.resizeColumnsToContents()
table.resizeRowsToContents()

window.resize(table.horizontalHeader().length() + 50, table.verticalHeader().length() + 50)

window.show()

# Lancer l'application
app.exec_()