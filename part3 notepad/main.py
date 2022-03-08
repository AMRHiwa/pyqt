from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt6.QtCore import QFileInfo
import sys

from NotePadApp import Ui_MainWindow

class NotePadWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionSave.triggered.connect(self.save_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionNew.triggered.connect(self.new_file)
        self.actionPrint.triggered.connect(self.print_file)
        self.actionPreview.triggered.connect(self.preview)
        self.actionExport_PDF.triggered.connect(self.export_pdf)
        self.actionExit.triggered.connect(self.quit)
        self.show()

    def quit(self):
        self.close()

    def export_pdf(self):
        file, ok = QFileDialog.getSaveFileName(self, "Export pdf", "PDF file (.pdf) ;; All files ()")
        if file != "":
            if QFileInfo(file).suffix() == "": file += ".pdf"
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(file)
            self.textEdit.document().print(printer)

    def preview(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintPreviewDialog(printer, self)
        dialog.paintRequested.connect(self.print_preview)
        dialog.exec()

    def print_preview(self, printer):
        self.textEdit.print(printer)

    def print_file(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer)

        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            self.textEdit.print(printer)

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

    def maybe_saved(self):
        if not self.textEdit.document().isModified():
            return True
        ret = QMessageBox.warning(self, "Application", "The document has been modified\nDo you want to save your changes ?",
                        QMessageBox.StandardButton.Save|QMessageBox.StandardButton.Discard|QMessageBox.StandardButton.Cancel)

        if ret == QMessageBox.StandardButton.Save:
            return self.save_file()
        if ret == QMessageBox.StandardButton.Cancel:
            return False

        return True

    def new_file(self):
        if self.maybe_saved():
            self.textEdit.clear()

app = QApplication(sys.argv)
notepad = NotePadWindow()
sys.exit(app.exec())