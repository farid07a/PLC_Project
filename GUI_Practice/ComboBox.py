from PyQt5.QtWidgets import QWidget,QApplication,QComboBox
import sys

app = QApplication(sys.argv)
window= QWidget()

window.resize(600,400)
window.move(120,120)

comb = QComboBox(window)
comb.move(50,50)

