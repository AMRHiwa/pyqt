from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 100, 400, 700)
        self.setWindowTitle("QGridLayout Example")
        self.setWindowIcon(QIcon("logo.png"))

        """
        QGridLayout
        We can Horizontal and vertical management of our window by QVBoxlayout.
        QGridLayout. First, We must to import QGridLayout from 
        QtWidgets, then we have to create a object of QGridLayout
        and then our objects relate to the this object
        for install QGridlayout to our window we have two way.

            First : 
                use QGridLayout for install to main window
                Object_name = QGridLayout(self)        

            Second :
                use setLayout(layout_object)
                QWidget or QmainWindow or ... _object.setLayout(layout_object)
        """
        # create a QGridLayout by QGridLayout(parent)
        grid = QGridLayout(self)

        # create many widgets
        btn1 = QPushButton("One")
        btn2 = QPushButton("Two")
        btn3 = QPushButton("Three")
        btn4 = QPushButton("Four")
        btn5 = QPushButton("Five")
        btn6 = QPushButton("Six")
        btn7 = QPushButton("Seven")
        btn8 = QPushButton("Eight")
        btn9 = QPushButton("Nine")

        # add widgets to gridlayout by addWidget(widget, Line number, Column number)
        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 0, 2)
        grid.addWidget(btn4, 1, 0)
        grid.addWidget(btn5, 1, 1)
        grid.addWidget(btn6, 1, 2)
        grid.addWidget(btn7, 2, 0)
        grid.addWidget(btn8, 2, 1)
        grid.addWidget(btn9, 2, 2)

        # grid.setRowStretch(0,1)
        # grid.setColumnStretch(0,1)

        self.show()
app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec())