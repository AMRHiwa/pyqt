from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qlabel Example")
        self.setGeometry(0,0,700,700)
        self.setWindowIcon(QIcon("image/logo.png"))

        """
        For create a label in pyqt, we must to create a variable
        then relate to this variable a QLabel Object. For this method
        we have two way to call it.
        
        The first way:
        name_variable = QLabel(the place that we want to install the label to it)
        
        The second way:
        name_variable = QLabel("the text that we want to show it on label",
                                 the place that we want to install the label to it)
        """
        
        label = QLabel("AMR Hiwa", self)

        # we can to install a different text to our label by "setText('tex')" method
        # label.setText("Mohamad Rasoul Azizi")
        
        # we can move the label by "move(x, y)" method
        label.move(100, 100)

        # we can set font for the our label's text by "setFont(QFont('family font', font-size))" method 
        # for that ability we have to import QFont from PyQt6.QtGui
        label.setFont(QFont("Arial", 15))

        # we can set color for our label's text by "setStyleSheet('color : color_name')" method
        label.setStyleSheet("color : red")

        # we can clear the label by "clear()" method
        # label.clear()
        

        """
        with label abiliy we can show image in window gui.
        For this work we have to import QPixmap from PyQt6.QtGui
        and create a variable to storage of image's address
        and also we need a variable to storage of label then relate to 
        pixmap's variable
        """
        
        # create a variable for label
        label2 = QLabel(self)

        # create a variable for pixmap
        pixmap = QPixmap('logo.png')

        # for set the pixmap object to label we use "setPixmap(pixmap_object_name)"
        label2.setPixmap(pixmap)
        label2.move(200,200)
        
        """
        we can also show the movie without sound by QMovie
        if we want to show multimedia we can use QMultiMedia
        for use this ability we must to import QMovie from PyQt6.QtGui
        and we must to create a variable to storage of QMovie object
        and we need to create and storage a object of label and QMovie variabl 
        relate to label object
        """
        
        # create a variable for label's object
        label3 = QLabel(self)

        # create a variable for QMovie's object
        movie = QMovie("images/sky.gif")

        # we can set speed of video 
        movie.setSpeed(200)

        # set movie to label
        label3.setMovie(movie)
        label3.move(300,400)


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec())