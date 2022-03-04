from PyQt6.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont, QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("logo.png"))
        self.setWindowTitle("QCalendarWidget Example")
        self.setGeometry(100, 100, 600, 500)

        vbox = QVBoxLayout()

        """
        QCalendarWidget
        import QCalendarWidget from PyQt.QtWidgets
        """
        # create the Calendar Object by QCalendarWidget(parent)
        self.calendar_widget = QCalendarWidget()

        # show the grids in calendar by setGridVisible(True) , it is false as default
        self.calendar_widget.setGridVisible(True)

        # connect the signal
        self.calendar_widget.selectionChanged.connect(self.show_date)

        self.label = QLabel("Hi")
        self.label.setFont(QFont("caveat", 15))
        self.label.setStyleSheet("color:green")

        vbox.addWidget(self.calendar_widget)
        vbox.addWidget(self.label)

        self.setLayout(vbox)
        self.show()

    def show_date(self):
        # for getting information from calendar we can use  selectedDate()
        mydate = self.calendar_widget.selectedDate()
        datestr = str(mydate.toPyDate())
        self.label.setText("date is : {}".format(datestr))

app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec())