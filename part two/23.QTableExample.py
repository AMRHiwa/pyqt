from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt6.QtGui import QFont, QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crud with QListWidget")
        self.setGeometry(100, 100, 600, 500)
        self.setWindowIcon(QIcon("logo.png"))

        vbox = QVBoxLayout()

        """
        QTableWidget
        for use this ability we can use QTableWidget that first we
        need to import QTableWidget and QTableWidgetItem from PyQt.QtWidgets
        """
        # create a QTableWidget object by QTableWidget(parent, rows, columns)
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(3)
        self.table_widget.setColumnCount(3)

        # add item in QTableWidget
        self.table_widget.setItem(0, 0, QTableWidgetItem("Name"))
        self.table_widget.setItem(0, 1, QTableWidgetItem("Email"))
        self.table_widget.setItem(0, 2, QTableWidgetItem("Phone"))
        self.table_widget.setItem(1, 0, QTableWidgetItem("Hiwa Azizi"))
        self.table_widget.setItem(1, 1, QTableWidgetItem("azizi.mr1377@gmail.com"))
        self.table_widget.setItem(1, 2, QTableWidgetItem("09189231264"))
        self.table_widget.setItem(2, 0, QTableWidgetItem("Milad HosseiniTabar"))
        self.table_widget.setItem(2, 1, QTableWidgetItem("Hosseini1375@gmail.com"))
        self.table_widget.setItem(2, 2, QTableWidgetItem("091096612364"))

        
        vbox.addWidget(self.table_widget)
        self.setLayout(vbox)
        self.show()

app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec())