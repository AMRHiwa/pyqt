# Form implementation generated from reading ui file '.\DBConnectionDemo.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(660, 296)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_create_db = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_create_db.setFont(font)
        self.pushButton_create_db.setObjectName("pushButton_create_db")

        # connect signal
        self.pushButton_create_db.clicked.connect(self.create_database)
        self.horizontalLayout_2.addWidget(self.pushButton_create_db)
        self.pushButton_connection_db = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_connection_db.setFont(font)
        self.pushButton_connection_db.setObjectName("pushButton_connection_db")

        # connect signal
        self.pushButton_connection_db.clicked.connect(self.db_connect)
        self.horizontalLayout_2.addWidget(self.pushButton_connection_db)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_result = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def db_connect(self):
        try:
            dbname = self.lineEdit.text()
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database=dbname
            )
            self.label_result.setText("There is connection")

        except mc.Error as e:
            self.label_result.setText("Connection Failed")

    def create_database(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password=""
            )
            cursor = mydb.cursor()
            dbname = self.lineEdit.text()
            cursor.execute(f"CREATE DATABASE {dbname}")
            self.label_result.setText(f"DataBase {dbname} Created")

        except mc.Error as e:
            self.label_result.setText("DataBase Creation Failed")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "DataBase Name :"))
        self.pushButton_create_db.setText(_translate("Form", "Create DataBase "))
        self.pushButton_connection_db.setText(_translate("Form", "DataBase Connection"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())