from PyQt6.QtWidgets import  QApplication, QWidget, QSpinBox, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSpinBox Example")
        self.setWindowIcon(QIcon("logo.png"))
        self.setGeometry(100, 100, 450, 450)

        self.create_object()

        self.show()
    def create_object(self):

        hbl = QHBoxLayout()
        self.label_price = QLabel("Laptop Price : ")
        self.label_price.setFont(QFont("caveat", 15, 700))

        self.lineEdit = QLineEdit()
        self.total_result = QLineEdit()

        """
        QSpinBox
        for use this ability you must import QSpinBox from QtWidgets
        and then need to create object from that
        """

        # create a QSpinBox object by QSpinBox(parent)
        self.spinbox_1 = QSpinBox()

        # can spinbox relate to a method by valueChanged.connect(method_name)
        self.spinbox_1.valueChanged.connect(self.spin_selected)

        hbl.addWidget(self.label_price)
        hbl.addWidget(self.lineEdit)
        hbl.addWidget(self.spinbox_1)
        hbl.addWidget(self.total_result )
        self.setLayout(hbl)

    def spin_selected(self):
        if int(self.lineEdit.text()) != 0:
            price = int(self.lineEdit.text())
            self.total_result.setText(str(price * self.spinbox_1.value()))
        else:
            self.total_result.setText("Wrong Number...!")
app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec())