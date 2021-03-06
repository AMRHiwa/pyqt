# Form implementation generated from reading ui file '.\Event.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(628, 409)
        Form.setWindowIcon(QtGui.QIcon("logo.png"))
        Form.setStyleSheet("background-color: cyan")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.change_btn = QtWidgets.QPushButton(Form)
        self.change_btn.clicked.connect(self.click_me)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.change_btn.setFont(font)
        self.change_btn.setObjectName("change_btn")
        self.horizontalLayout.addWidget(self.change_btn)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:lightblue")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Raleway SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: red;\n"
"\n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QtDesiger Application"))
        self.change_btn.setText(_translate("Form", "Click ME"))
        self.lineEdit.setPlaceholderText(_translate("Form", "please Enter your name"))
        self.label.setText(_translate("Form", "TextLabel"))

    def click_me(self):
        text = self.lineEdit.text()
        self.label.setText(text)
        self.label.setFont(QtGui.QFont("Times", 16))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
