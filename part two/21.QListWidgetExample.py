from PyQt6.QtWidgets import QApplication, QWidget, QListWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont, QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 550, 200)
        self.setWindowIcon(QIcon("logo.png"))
        self.setWindowTitle("QListWidget Example")

        vbx = QVBoxLayout()
        """
        QListWidget
        we
        """
        # create a listWidget object by QListWidget(parent)
        self.listWidget = QListWidget()

        # inserting data to our listWidget by insertItem(number_of_row, "item_name")
        self.listWidget.insertItem(0, "Python")
        self.listWidget.insertItem(1, "Java")
        self.listWidget.insertItem(2, "JavaScript")
        self.listWidget.insertItem(3, "C#")
        self.listWidget.insertItem(1, "Kotlin")

        # set font for listWidget by setFont(QFont("font-family", font-size))
        self.listWidget.setFont(QFont("caveat", 14))

        # set background's color for listWidget by setStyleSheet("background-color: color-name")
        self.listWidget.setStyleSheet("background-color : pink")

        # for connecting listWidget to one function you must use the clicked.connect(func-name)
        self.listWidget.clicked.connect(self.listWidget_choose)

        self.label_result = QLabel("choose one item ...")
        self.label_result.setFont(QFont("caveat", 17))

        vbx.addWidget(self.listWidget)
        vbx.addWidget(self.label_result)
        self.setLayout(vbx)
        self.show()

    def listWidget_choose(self):
        item = self.listWidget.currentItem()
        self.label_result.setText("you choose the " + str(item.text()))

app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec())