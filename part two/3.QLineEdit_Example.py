from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtGui import QIcon, QFont
# from PyQt6.QtCore import
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLineEdit Example")
        self.setGeometry(200, 100, 400, 700)
        self.setWindowIcon(QIcon("logo.png"))

        """
        QLineEdit
        we can use lineedit in our window's program
        for use this ability you must import QlineEdit from QtWidget
        first, we must create a variable to storage QLineEdit object
        """

        # create a QLineEdit by QLineEdit(parent)
        line_edit = QLineEdit(self)

        # set font for lineEdit's Text by setFont(QFont("family_font", font-size))
        line_edit.setFont(QFont("Sanserif", 16))

        # set default text for our LineEdit by setText("text")
        # line_edit.setText("Default Text")

        # set place holder Text for our lineEdit by setPlaceholderText("text")
        line_edit.setPlaceholderText("enter the your name")

        # change ability write in lineedit by setEnabled(False or True)
        # line_edit.setEnabled(False)

        # you can change the lineedit echo mode for entering password
        # line_edit.setEchoMode(QLineEdit.EchoMode.Password)    

        self.show()

app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec())