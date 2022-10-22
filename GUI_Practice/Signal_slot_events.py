import sys

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton

class WindowClassWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(700,500)
        self.setWindowTitle("Events Code")
        btn = QPushButton('Click',self)
        btn.setCheckable(True)
        btn.clicked.connect(self.the_button_was_clicked)
        btn.clicked.connect(self.the_button_was_toggled)

    def the_button_was_clicked(self):
        print("clicked")
    def the_button_was_toggled(self,checked):
        print("checked",checked)



app = QApplication(sys.argv)

WindowClassWidget_obj=WindowClassWidget()
WindowClassWidget_obj.show()

app.exec_()