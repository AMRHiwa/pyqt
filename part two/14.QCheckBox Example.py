from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 100, 400, 400)
        self.setWindowTitle("QCheckBox Example")
        self.setWindowIcon(QIcon("logo.png"))

        """
        QCheckBox 
        for using this ability you must import QCheckBox from QtWidgets
        and neet to create a object of QCheckBox 
        """
        hbxl = QHBoxLayout()

        # for creating a object of QCheckBox you must use QCheckBox("text", parent)
        self.checkbox_py = QCheckBox("Python")

        # we can set icon for checkbox widget by setIcon(QIcon("address and name"))
        self.checkbox_py.setIcon(QIcon("images/py.png"))

        # we can set font for our checkbox by setFont(QFont("font-family", font-size))
        self.checkbox_py.setFont(QFont("Times", 15))

        # we can change checkbox icon size by setIconSize(QSize(size_of_x, size_of_y))
        self.checkbox_py.setIconSize(QSize(30, 30))

        # for connect a function to our checkbox we can use stateChanged.connect(method_name)
        self.checkbox_py.stateChanged.connect(self.checkbox_checked)

        self.checkbox_java = QCheckBox("Java")
        self.checkbox_java.setFont(QFont("Times", 15))
        self.checkbox_java.setIcon(QIcon("images/java.png"))
        self.checkbox_java.setIconSize(QSize(30, 30))
        self.checkbox_java.stateChanged.connect(self.checkbox_checked)

        self.checkbox_js = QCheckBox("JavaScript")
        self.checkbox_js.setFont(QFont("Times", 15))
        self.checkbox_js.setIcon(QIcon("images/javascript.png"))
        self.checkbox_js.setIconSize(QSize(30, 30))
        self.checkbox_js.stateChanged.connect(self.checkbox_checked)

        self.label_result = QLabel("")
        self.label_result.setFont(QFont("Times", 15))

        # add widgets to QHBoxLayout
        hbxl.addWidget(self.checkbox_py)
        hbxl.addWidget(self.checkbox_java)
        hbxl.addWidget(self.checkbox_js)

        vbxl = QVBoxLayout()
        # add label widget to QVBoxLayout
        vbxl.addWidget(self.label_result)
        # add QHBoxLayout to QVBoxLayout
        vbxl.addLayout(hbxl)

        # setting the vertical layout to our window object
        self.setLayout(vbxl)

        self.show()

    def checkbox_checked(self):
        selected1 = ""
        selected2 = ""
        selected3 = ""
        if self.checkbox_py.isChecked():
            selected1 = "Python"
        if self.checkbox_java.isChecked():
            selected2 = "Java"
        if self.checkbox_js.isChecked():
            selected3 = "JavaScript"
        self.label_result.setText(f"you choose : {selected1} {selected2} {selected3}")

app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec())