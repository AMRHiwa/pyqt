from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QListWidget
from PyQt6 import uic
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("QListWidgetExample.ui", self)
        self.labelResult = self.findChild(QLabel, "label_result")
        self.listbox = self.findChild(QListWidget, "listWidget")
        self.listbox.clicked.connect(self.listWidget_changed)
        self.show()

    def listWidget_changed(self):
        item = self.listbox.currentItem()
        self.labelResult.setText("You choose the : " + str(item.text()))
        
app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec())