# Form implementation generated from reading ui file '.\QRadioButton_Exmaple_Type_Flight_UI.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(423, 364)
        Dialog.setStyleSheet("QDialog\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    color: rgb(255, 255, 0);\n"
"}")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_first_class = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_first_class.setFont(font)
        self.radioButton_first_class.setObjectName("radioButton_first_class")
        self.radioButton_first_class.toggled.connect(self.radiobutton_clicked)
        self.verticalLayout.addWidget(self.radioButton_first_class)
        self.radioButton_busniess_class = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_busniess_class.setFont(font)
        self.radioButton_busniess_class.setObjectName("radioButton_busniess_class")
        self.radioButton_busniess_class.toggled.connect(self.radiobutton_clicked)
        self.verticalLayout.addWidget(self.radioButton_busniess_class)
        self.radioButton_economy_class = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_economy_class.setFont(font)
        self.radioButton_economy_class.setObjectName("radioButton_economy_class")
        self.radioButton_economy_class.toggled.connect(self.radiobutton_clicked)
        self.verticalLayout.addWidget(self.radioButton_economy_class)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_result = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout_2.addWidget(self.label_result)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "QRadioButton Example"))
        self.label.setText(_translate("Dialog", "select flight type :"))
        self.radioButton_first_class.setText(_translate("Dialog", "First Class                 $150"))
        self.radioButton_busniess_class.setText(_translate("Dialog", "Busniess Class           $120"))
        self.radioButton_economy_class.setText(_translate("Dialog", "Economy Class          $100"))

    def radiobutton_clicked(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.label_result.setText(f"you have choice : {radio_btn.text()}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
