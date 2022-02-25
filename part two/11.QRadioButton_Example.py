from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRadioButton Example")
        self.setGeometry(200, 100, 400, 700)
        self.setWindowIcon(QIcon("logo.png"))
        self.create_radio()


        self.show()

    def create_radio(self):
        HBXL = QHBoxLayout()
        # self.label = QLabel("default Text")

        """
        QRadioButton
        You can use RadioButton ability by QRadioButton.
        you must import QRadioButton from QtWidgets.
        then you have to create a object from that
        """

        # create a RadioButton by QRadioButton("text", parent)
        radio_button_python = QRadioButton("Python")

        # set icon for radiobutton by setIcon(QIcon("address and name"))
        radio_button_python.setIcon(QIcon("images/py.png"))

        # we can set size for icon by setIconSize(QSize(size_of_x, size_of_y))
        radio_button_python.setIconSize(QSize(30,30))

        # wa can set font for radiobutton by setFont(QFont("font-family", font-size))
        radio_button_python.setFont(QFont("Times", 14))

        # we can set a default for our radiobutton by setChecked(False or True)
        radio_button_python.setChecked(True)

        # can install a function to our radio_button by toggled.connect(function_name)
        radio_button_python.toggled.connect(self.radio_selected)


        radio_button_java = QRadioButton("Java")
        radio_button_java.setIcon(QIcon("images/java.png"))
        radio_button_java.setIconSize(QSize(30,30))
        radio_button_java.setFont(QFont("Times", 14))
        radio_button_java.toggled.connect(self.radio_selected)

        radio_button_javaScript = QRadioButton("JavaScript")
        radio_button_javaScript.setIcon(QIcon("images/javascript.png"))
        radio_button_javaScript.setIconSize(QSize(30, 30))
        radio_button_javaScript.setFont(QFont("Times", 14))
        radio_button_javaScript.toggled.connect(self.radio_selected)

        self.label = QLabel()
        self.label.setFont(QFont("arial", 14))
        self.label.setStyleSheet("color : green")

        # add widget to layout
        HBXL.addWidget(radio_button_python)
        HBXL.addWidget(radio_button_java)
        HBXL.addWidget(radio_button_javaScript)

        # create a vertical layout
        VBXL = QVBoxLayout()

        # add HBXL (HorizontalBoxLayout) to Vertical layout
        VBXL.addLayout(HBXL)

        # add widgets to Vertical layout
        VBXL.addWidget(self.label)

        # set VBXL (VerticalBoxLayout) to our window
        self.setLayout(VBXL)

    def radio_selected(self):
        # we can send our radion_button object that is selected to the variable by sender() method
        radio_btn = self.sender()

        # for checking that our radio_button is select or not we can use isChecked() method
        if radio_btn.isChecked():
            self.label.setText(f"you have selected : {radio_btn.text()}")


app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec())