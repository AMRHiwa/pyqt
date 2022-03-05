from PyQt6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLabel, QLineEdit,\
    QInputDialog, QPushButton, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QInputDialog Example")
        self.setGeometry(100, 100, 600, 500)
        self.setWindowIcon(QIcon("logo.png"))

        self.create_input_dialog()

        self.show()

    def create_input_dialog(self):
        hbox = QHBoxLayout()

        self.label = QLabel("Choose the Country : ")
        self.label.setFont(QFont("Times", 15))

        self.lineEdit = QLineEdit()
        self.lineEdit.setFont(QFont("times", 12))

        self.btn_item = QPushButton("Choose the Country")
        self.btn_item.setFont(QFont("Times", 12))
        self.btn_item.clicked.connect(self.get_item)

        self.btn_text = QPushButton("Enter Country Name")
        self.btn_text.setFont(QFont("Times", 12))
        self.btn_text.clicked.connect(self.get_text)

        self.btn_num = QPushButton("Enter Country Number")
        self.btn_num.setFont(QFont("Times", 12))
        self.btn_num.clicked.connect(self.get_num)


        hbox.addWidget(self.label)
        hbox.addWidget(self.lineEdit)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.btn_item)
        vbox.addWidget(self.btn_text)
        vbox.addWidget(self.btn_num)
        self.setLayout(vbox)

    def get_item(self):
        countries = [ "Iran", "United States", "United Kingdom", "Afghanistan",
                      "Russia", "Chaine", "Ukraine"]
        country,ok = QInputDialog.getItem(self, "Input Dialog", "List of Countries", countries, 0, False)
        if ok and country:
            self.lineEdit.setText(country)

    def get_text(self):
        mytext, ok = QInputDialog.getText(self, "Country Name", "Enter the Country name : ")
        if mytext and ok :
            self.lineEdit.setText(mytext)

    def get_num(self):
        mynumber, ok = QInputDialog.getInt(self, "Country Number", "Enter the Number : ", 1, 2, 3, 4)
        if mynumber and ok:
            self.lineEdit.setText(str(mynumber))
            
app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec())