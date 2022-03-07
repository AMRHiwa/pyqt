from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import sys

from NotePadApp import Ui_MainWindow

class NotePadWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionSave.triggered.connect(self.save_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.show()


    def save_file(self):
        filename = QFileDialog.getSaveFileName(self, "Save File")

        if filename[0]:
            f = open(filename[0], "w")
            with f:
                text = self.textEdit.toPlainText()
                f.write(text)
                QMessageBox.about(self, "Save File", "File has been saved")

    def open_file(self):
        filename = QFileDialog.getOpenFileName(self, "Open File")
        if filename[0]:
            f = open(filename[0], "r")
            text = f.read()
            self.textEdit.setText(text)
            QMessageBox.about(self, "Open file", "File has been opened")
app = QApplication(sys.argv)
notepad = NotePadWindow()
sys.exit(app.exec())