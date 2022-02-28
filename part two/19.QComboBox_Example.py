from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 200)
        self.setWindowTitle("QComboBox Example")
        self.setWindowIcon(QIcon("logo.png"))
        self.create_combo()
        self.show()

    def create_combo(self):
        hbx = QHBoxLayout()

        self.label = QLabel("Choose Account Type : ")
        self.label.setFont(QFont("caveat", 22, weight=600))

        """
        QComboBox 
        we can use combobox ability by QComboBox that need to import it
        from QtWidgets. first we must to create a object from that.
        """
        # create a QComboBox by QComboBox(parent)
        self.combobox = QComboBox()

        # add item to combobox by addItem("text")
        self.combobox.addItem("Current Account")
        self.combobox.addItem("Deposit Account")
        self.combobox.addItem("Saving Account")

        # for connecting combobox to a function when it's item change
        # we can use currentTextChanged.connect(function_name)
        self.combobox.currentTextChanged.connect(self.combo_changing)

        hbx.addWidget(self.label)
        hbx.addWidget(self.combobox)

        vbx = QVBoxLayout()

        self.label_result = QLabel("")
        self.label_result.setFont(QFont("caveat", 19))

        vbx.addLayout(hbx)
        vbx.addWidget(self.label_result)
        self.setLayout(vbx)

    def combo_changing(self):
        item = self.combobox.currentText()
        self.label_result.setText("Your account type is : " + item)


app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec())
