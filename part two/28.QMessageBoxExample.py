# Form implementation generated from reading ui file '.\QMessageBoxExampleUI.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

"""
QMessageBox
for this ability you must import it from PyQt.QtWidget
and make for :
    1.Warning Message:
        for this work we have to create a warning messagebox with
        QMessageBox.warning(parent, "Title", "Message")
    2.Information Message:
        for this work we have to create a information messagebox with
        QMessageBox.information(parent, "Title", "Message")
    3.About Message:
        for this work we have to create a About messagebox with
        QMessageBox.about(parent, "Title", "Message")
"""

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog, QMessageBox


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(406, 301)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_warning = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_warning.setFont(font)
        self.pushButton_warning.setObjectName("pushButton_warning")

        # connect signal
        self.pushButton_warning.clicked.connect(self.btn_warning)

        self.verticalLayout.addWidget(self.pushButton_warning)
        self.pushButton_info = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_info.setFont(font)
        self.pushButton_info.setObjectName("pushButton_info")

        # connect signal
        self.pushButton_info.clicked.connect(self.btn_information)

        self.verticalLayout.addWidget(self.pushButton_info)
        self.pushButton_about = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_about.setFont(font)
        self.pushButton_about.setObjectName("pushButton_about")
        self.verticalLayout.addWidget(self.pushButton_about)

        # connect signal
        self.pushButton_about.clicked.connect(self.btn_about)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def btn_warning(self):
        QMessageBox.warning(self, "Warning...", "This is a warning message!")

    def btn_information(self):
        QMessageBox.information(self, "Information...", "This is a information message!")

    def btn_about(self):
        QMessageBox.about(self, "About...", "This is a about message!")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "QMessageBox Example"))
        self.pushButton_warning.setText(_translate("Dialog", "Warning!"))
        self.pushButton_info.setText(_translate("Dialog", "Information !"))
        self.pushButton_about.setText(_translate("Dialog", "About ?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())