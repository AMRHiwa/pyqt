# Form implementation generated from reading ui file '.\QComboBox_designer_DEMO.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 200)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentTextChanged.connect(self.combo_changing)
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_result = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def combo_changing(self):
        item = self.comboBox.currentText()
        self.label_result.setText("Your Favorite language is {}".format(item))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QComboBox_designer_DEMO"))
        self.label.setText(_translate("Form", "choose your favorite language :"))
        self.comboBox.setItemText(0, _translate("Form", "Python"))
        self.comboBox.setItemText(1, _translate("Form", "Java"))
        self.comboBox.setItemText(2, _translate("Form", "C++"))
        self.comboBox.setItemText(3, _translate("Form", "C#"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
