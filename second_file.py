from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.statusBar().showMessage("This application developed by AMR Hiwa")
window.menuBar().addMenu("file")
window.show()
sys.exit(app.exec())