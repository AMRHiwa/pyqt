from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPushButton Example")
        self.setGeometry(200, 200, 700, 400 )
        self.setWindowIcon(QIcon('logo.png'))

        """
        For create a PushButton in pyqt we must call QPushButton 
        from QtWidget . we have to create a variable to storage
        object of pushbutton in itself
        """
        # for make a pushbutton we must call QPushButton("text on button", parent)
        push1 = QPushButton("click", self)

        # we can set geometry for this button by setGeometry(x, y, width, height)
        push1.setGeometry(100, 50, 100, 70)

        # we can set font for our PushButton text by setFont(QFont("font_family", font-size [,QFont.Weight.bold or ...]))
        # we must call Qfont from QtGui
        push1.setFont(QFont("Times", 12, QFont.Weight.Bold))

        # also we can change the PushButton's background color
        # push1.setStyleSheet("background-color: lightblue")

        # can set Icon for our pushbutton by setIcon(QIcon("icon_address"))
        push1.setIcon(QIcon('images/python.png'))

        # can set size for Pushbutton's Icon by setIconSize(QSize(x, y))
        # first, must to call QSize from QtCore
        push1.setIconSize(QSize(40,40))

        # can set popup menu for our PushButton by create menu object
        # first we must call QMenu from QtWidgets and creat a variable for Menu Object by QMenu(parent)
        menu = QMenu(self)

        # can set font for our PushButton's menu
        menu.setFont(QFont("Times", 10, QFont.Weight.Bold))

        # can change menu's background color by setStyleSheet("background-color : color_name")
        menu.setStyleSheet("background-color: red")

        # add many Action to my menu
        menu.addAction("Action 1")
        menu.addAction("Action 2")
        menu.addAction("Action 3")

        # now we set menu to our PushButton by setMenu(menu)
        push1.setMenu(menu)

        self.show()

app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec())