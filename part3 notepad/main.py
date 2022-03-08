from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QFontDialog, QColorDialog, QDialog
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import QFileInfo, Qt
import sys

from NotePadApp import Ui_MainWindow

class NotePadWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("images/applogo.png"))
        self.setupUi(self)
        self.actionSave.triggered.connect(self.save_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionNew.triggered.connect(self.new_file)
        self.actionPrint.triggered.connect(self.print_file)
        self.actionPreview.triggered.connect(self.preview)
        self.actionExport_PDF.triggered.connect(self.export_pdf)
        self.actionExit.triggered.connect(self.quit)
        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionRedo.triggered.connect(self.textEdit.redo)
        self.actionCut.triggered.connect(self.textEdit.cut)
        self.actionCopy.triggered.connect(self.textEdit.copy)
        self.actionPaste.triggered.connect(self.textEdit.paste)
        self.actionBold.triggered.connect(self.make_bold)
        self.actionItalic.triggered.connect(self.make_italic)
        self.actionUnderline.triggered.connect(self.make_underline)
        self.actionRight_2.triggered.connect(self.make_right_text)
        self.actionLeft_2.triggered.connect(self.make_left_text)
        self.actionCenter.triggered.connect(self.make_center_text)
        self.actionJustify.triggered.connect(self.make_justify_text)
        self.actionColor.triggered.connect(self.color_dialog)
        self.actionFont.triggered.connect(self.font_dialog)
        self.actionAbout_App.triggered.connect(self.about)
        self.show()
    def font_dialog(self):
        font, ok = QFontDialog.getFont()
        if font and ok:
            self.textEdit.setFont(font)

    def color_dialog(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    def about(self):
        QMessageBox.about(self, "About This app", "This app developed by AMR Hiwa\nNotepad program")
    def make_right_text(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignRight)

    def make_left_text(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def make_center_text(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def make_justify_text(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignJustify)

    def make_underline(self):
        font = QFont()
        font.setUnderline(True)
        self.textEdit.setFont(font)

    def make_italic(self):
        font = QFont()
        font.setItalic(True)
        self.textEdit.setFont(font)

    def make_bold(self):
        font = QFont()
        font.setBold(True)
        self.textEdit.setFont(font)
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