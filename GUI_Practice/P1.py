
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton



def prepareGui():
    app= QApplication(sys.argv)  # gui for append all component sys.argv attach sys with prg
    window = QWidget()   # create window
    window.resize(400,500)
    # window.setWindowIcon(QIcon('Control.png')) # icon of window
    window.move(150,150) # x ,y of window
    window.setToolTip("Main Program")

    btn = QPushButton('Click',window)

    btn.resize(80,40)
    btn.move(40,60)
    btn.setToolTip("Clik to btn")
    btn.clicked.connect(print_events)
    window.show()
    #window.setGeometry(400,400,600,600)
    window.setWindowTitle("hello by QT")
    app.exec_() # main loop to create all compent in window and display in  app
                # exec_() for Qt and exec() reserverd word for python

def print_events():
    print(" test events ")



if __name__ == "__main__":
    prepareGui()