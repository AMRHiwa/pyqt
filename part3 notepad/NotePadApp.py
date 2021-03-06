# Form implementation generated from reading ui file '.\NotePadAppDesign.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuFormat = QtWidgets.QMenu(self.menubar)
        self.menuFormat.setObjectName("menuFormat")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionNew = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/new.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/open.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/save.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionPrint = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/print.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPrint.setIcon(icon3)
        self.actionPrint.setObjectName("actionPrint")
        self.actionPreview = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/printprev.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPreview.setIcon(icon4)
        self.actionPreview.setObjectName("actionPreview")
        self.actionExport_PDF = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/pdf.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExport_PDF.setIcon(icon5)
        self.actionExport_PDF.setObjectName("actionExport_PDF")
        self.actionExit = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExit.setIcon(icon6)
        self.actionExit.setObjectName("actionExit")
        self.actionUndo = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/undo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionUndo.setIcon(icon7)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/redo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionRedo.setIcon(icon8)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/cut.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCut.setIcon(icon9)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("images/copy.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCopy.setIcon(icon10)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("images/paste.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPaste.setIcon(icon11)
        self.actionPaste.setObjectName("actionPaste")
        self.actionBold = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("images/bold.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionBold.setIcon(icon12)
        self.actionBold.setObjectName("actionBold")
        self.actionItalic = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("images/italic.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionItalic.setIcon(icon13)
        self.actionItalic.setObjectName("actionItalic")
        self.actionUnderline = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("images/underline.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionUnderline.setIcon(icon14)
        self.actionUnderline.setObjectName("actionUnderline")
        self.actionLeft = QtGui.QAction(MainWindow)
        self.actionLeft.setObjectName("actionLeft")
        self.actionRight = QtGui.QAction(MainWindow)
        self.actionRight.setObjectName("actionRight")
        self.actionLeft_2 = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("images/left.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionLeft_2.setIcon(icon15)
        self.actionLeft_2.setObjectName("actionLeft_2")
        self.actionRight_2 = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("images/right.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionRight_2.setIcon(icon16)
        self.actionRight_2.setObjectName("actionRight_2")
        self.actionCenter = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("images/center.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCenter.setIcon(icon17)
        self.actionCenter.setObjectName("actionCenter")
        self.actionJustify = QtGui.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("images/justify.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionJustify.setIcon(icon18)
        self.actionJustify.setObjectName("actionJustify")
        self.actionFont = QtGui.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("images/font.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionFont.setIcon(icon19)
        self.actionFont.setObjectName("actionFont")
        self.actionColor = QtGui.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("images/color.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionColor.setIcon(icon20)
        self.actionColor.setObjectName("actionColor")
        self.actionAbout_App = QtGui.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("images/aboutqt.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAbout_App.setIcon(icon21)
        self.actionAbout_App.setObjectName("actionAbout_App")
        self.menufile.addAction(self.actionNew)
        self.menufile.addAction(self.actionOpen)
        self.menufile.addAction(self.actionSave)
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionPrint)
        self.menufile.addAction(self.actionPreview)
        self.menufile.addAction(self.actionExport_PDF)
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuFormat.addAction(self.actionBold)
        self.menuFormat.addAction(self.actionItalic)
        self.menuFormat.addAction(self.actionUnderline)
        self.menuFormat.addSeparator()
        self.menuFormat.addAction(self.actionLeft_2)
        self.menuFormat.addAction(self.actionRight_2)
        self.menuFormat.addAction(self.actionCenter)
        self.menuFormat.addAction(self.actionJustify)
        self.menuFormat.addSeparator()
        self.menuFormat.addAction(self.actionFont)
        self.menuFormat.addAction(self.actionColor)
        self.menuAbout.addAction(self.actionAbout_App)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFormat.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionBold)
        self.toolBar.addAction(self.actionItalic)
        self.toolBar.addAction(self.actionUnderline)
        self.toolBar.addAction(self.actionLeft_2)
        self.toolBar.addAction(self.actionCenter)
        self.toolBar.addAction(self.actionRight_2)
        self.toolBar.addAction(self.actionJustify)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionFont)
        self.toolBar.addAction(self.actionColor)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NotePad App"))
        self.menufile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuFormat.setTitle(_translate("MainWindow", "Format"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionPreview.setText(_translate("MainWindow", "Preview"))
        self.actionPreview.setShortcut(_translate("MainWindow", "Ctrl+Shift+P"))
        self.actionExport_PDF.setText(_translate("MainWindow", "Export PDF"))
        self.actionExport_PDF.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionBold.setText(_translate("MainWindow", "Bold"))
        self.actionBold.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.actionItalic.setText(_translate("MainWindow", "Italic"))
        self.actionItalic.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionUnderline.setText(_translate("MainWindow", "Underline"))
        self.actionUnderline.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionLeft.setText(_translate("MainWindow", "Left"))
        self.actionRight.setText(_translate("MainWindow", "Right"))
        self.actionLeft_2.setText(_translate("MainWindow", "Left"))
        self.actionLeft_2.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionRight_2.setText(_translate("MainWindow", "Right"))
        self.actionRight_2.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionCenter.setText(_translate("MainWindow", "Center"))
        self.actionCenter.setShortcut(_translate("MainWindow", "Ctrl+K"))
        self.actionJustify.setText(_translate("MainWindow", "Justify"))
        self.actionJustify.setShortcut(_translate("MainWindow", "Ctrl+J"))
        self.actionFont.setText(_translate("MainWindow", "Font"))
        self.actionColor.setText(_translate("MainWindow", "Color"))
        self.actionAbout_App.setText(_translate("MainWindow", "About App"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
