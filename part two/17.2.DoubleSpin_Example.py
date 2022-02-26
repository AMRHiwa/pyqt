from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QDoubleSpinBox, QLineEdit
from PyQt6.QtGui import QFont, QIcon
from PyQt6 import uic
import sys
"""
uic
for accessing to the file.ui in python file
you have to import uic from PyQt and you can import .ui file
"""
class UI(QWidget):
    def __init__(self):
        super().__init__()

        # import ui file by uic.loadUi("name and address", parent)
        uic.loadUi("DoubleSpinDemo.ui", self)

        # for accessing to .ui's widget you can use findChild(type_widget, "widget's name")
        self.lineEdit_price = self.findChild(QLineEdit, "lineEdit_price")
        self.doubleSpin = self.findChild(QDoubleSpinBox, "doubleSpinBox")
        self.doubleSpin.valueChanged.connect(self.doublespin_changed)
        self.lineEdit_total = self.findChild(QLineEdit, "lineEdit_total")
        self.show()
    def doublespin_changed(self):
        price = int(self.lineEdit_price.text())
        self.lineEdit_total.setText(f"{price * self.doubleSpin.value()}")
app = QApplication(sys.argv)
screen = UI()
sys.exit(app.exec())