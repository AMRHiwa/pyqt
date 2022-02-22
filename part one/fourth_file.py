from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,700,400)
        self.setFixedSize(700, 400)
        self.setWindowTitle("python GUI development")
        self.setWindowIcon(QIcon("image/logo.png"))
        self.setStyleSheet("background-color: pink")
        # self.setWindowOpacity(0.7)

        self.show()


app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec())