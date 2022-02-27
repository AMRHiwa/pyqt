from PyQt6.QtWidgets import QApplication, QWidget, QLCDNumber, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QTime, QTimer
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLCDNumber Example")
        self.setWindowIcon(QIcon("logo.png"))
        self.setGeometry(100, 100, 250, 150)
        # for getting time every second we need a timer to do a function
        # we must create timer object from QTimer that first we need to import that from PyQt.QtCore
        timer = QTimer()
        # for connecting the timer to the one function we can use timeout.connect("function_name")
        timer.timeout.connect(self.create_widget)
        # also we can set the time do one thing to do it every any time we need
        timer.start(1000)
        self.create_widget()
        self.show()

    def create_widget(self):
        vbx = QVBoxLayout()
        """
        QLCDNumber
        we can use this ability by import QLCDNumber from QtWidget
        then we must to create a lcdnumber object
        """
        # create a QLCDNumber by QLCDNumber(parent)
        lcd = QLCDNumber()
        # for getting current time we have to use QTime.currentTime() method
        # first we have to import QTime from PyQt.QtCore
        time = QTime.currentTime()
        # transform object time to the string of time by toString("time_format")
        text = time.toString("hh:mm")
        # for showing one thing in LCDNumber we must use display("object_name")
        lcd.display(text)

        vbx.addWidget(lcd)
        self.setLayout(vbx)


app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec())