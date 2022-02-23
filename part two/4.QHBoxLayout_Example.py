from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBoxLayout Example")
        self.setGeometry(200, 100, 400, 700)
        self.setWindowIcon(QIcon("logo.png"))

        """
        QHBoxLayout
        for Horizontal management of our window we can use 
        QHBoxLayout. First, We must to import QHBoxLayout from 
        QtWidgets, then we have to create a object of QHBoxLayout
        and then our objects relate to the this object
        for install QHBoxlayout to our window we have two way.
            
            First : 
                use QHBoxLayout for install to main window
                Object_name = QHBoxLayout(self)        

            Second :
                use setLayout(layout_object)
                QWidget or QmainWindow or ... _object.setLayout(layout_object)            
        """
        # create a QHBoxLayout by QHBoxLayout(parent)
        QHBL = QHBoxLayout(self)

        # create many widget to install to QHBoxLayout
        push1 = QPushButton("One")
        push2 = QPushButton("Two")
        push3 = QPushButton("Three")
        push4 = QPushButton("Four")
        push5 = QPushButton("Five")

        # we add widgets to QHBoxLayout
        QHBL.addWidget(push1)
        QHBL.addWidget(push2)
        QHBL.addWidget(push3)
        QHBL.addWidget(push4)

        # we can make space between item in layout by addSpacing(size)
        QHBL.addSpacing(50)

        QHBL.addWidget(push5)

        # QHBL.addStretch(500)

        # second way to install layout to our window
        # self.setLayout(QHBL)

        self.show()

app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec())