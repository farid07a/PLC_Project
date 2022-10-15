from PyQt5.QtWidgets import  *

app = QApplication([])
btn=QPushButton('clik')
def click_btn():
    alert=QMessageBox()
    alert.setText('Your cicked ')
    alert.exec()


btn.clicked.connect(click_btn)
btn.show()
app.exec()


