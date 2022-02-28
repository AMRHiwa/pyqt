from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLabel
from PyQt6 import uic
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("QComboBox_designer_DEMO.ui",self)

        self.combo = self.findChild(QComboBox, "comboBox")
        self.combo.currentTextChanged.connect(self.combo_change)
        self.label_rsult = self.findChild(QLabel, "label_result")
        self.show()

    def combo_change(self):
        item = self.combo.currentText()
        self.label_rsult.setText("your favorite language is : " + item)

app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec())
