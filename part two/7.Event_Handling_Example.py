from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 700)
        self.setWindowTitle("Event Handling Example")
        self.setWindowIcon(QIcon("logo.png"))

        self.create_widget()

        self.show()

    def create_widget(self):
        qvbl = QVBoxLayout()
        btn = QPushButton("Change Text")
        # for PushButton click Event we can use from under formula
        # pushbutton_object.clicked.connect(function_name)
        btn.clicked.connect(self.clicked_btn)
        self.label1 = QLabel("Default Text")

        qvbl.addWidget(self.label1)
        qvbl.addWidget(btn)

        self.setLayout(qvbl)

    def clicked_btn(self):
        self.label1.setText("label changed")
        self.label1.setFont(QFont("Arials", 15))
        self.label1.setStyleSheet("color : red")

app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec())