from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QVBoxLayout Example")
        self.setGeometry(200, 100, 400, 700)
        self.setWindowIcon(QIcon("logo.png"))

        """
        QVBoxLayout
        We can vertical management of our window by QVBoxlayout.
        QVBoxLayout. First, We must to import QVBoxLayout from 
        QtWidgets, then we have to create a object of QVBoxLayout
        and then our objects relate to the this object
        for install QVBoxlayout to our window we have two way.
            
            First : 
                use QVBoxLayout for install to main window
                Object_name = QVBoxLayout(self)        

            Second :
                use setLayout(layout_object)
                QWidget or QmainWindow or ... _object.setLayout(layout_object)
        """
        # create a QVBoxLayout by QVBoxLayout(parent)
        QVBL = QVBoxLayout(self)

        # make many widgets
        push1 = QPushButton("One")
        push2 = QPushButton("Two")
        push3 = QPushButton("Three")
        push4 = QPushButton("Four")
        push5 = QPushButton("Five")


        # we add widgets to QVBoxLayout
        QVBL.addWidget(push1)
        QVBL.addWidget(push2)
        QVBL.addWidget(push3)
        QVBL.addWidget(push4)

        # we can make space between item in layout by addSpacing(size)
        # QVBL.addSpacing(50)

        QVBL.addWidget(push5)

        QVBL.addStretch()

        # second way to install layout to our window
        # self.setLayout(QVBL)

        self.show()


app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec())