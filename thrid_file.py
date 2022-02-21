from PyQt6.QtWidgets import QApplication, QDialog
import sys

app = QApplication(sys.argv)
window = QDialog()

# window.statusBar().showMessage("AMR Hiwa")
# AttributeError: 'QDialog' object has no attribute 'statusBar

# window.menuBar().addMenu("file")
# AttributeError: 'QDialog' object has no attribute 'menuBar'

window.show()
sys.exit(app.exec())