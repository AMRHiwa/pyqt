from PyQt6.QtWidgets import QApplication, QWidget
import sys


app = QApplication(sys.argv)

window = QWidget()

# window.statusBar().showMessage("This application developed by AMR Hiwa")      
# AttributeError: 'QWidget' object has no attribute 'statusBar'

# window.menuBar().addMenu("file")
# AttributeError: 'QWidget' object has no attribute 'menuBar'
window.show()
sys.exit(app.exec())