from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox
import sys

app = QApplication(sys.argv)
window= QWidget()

window.setGeometry(100,100,400,500)
chbx = QCheckBox(window, text='Ios')

chbx.move(60,60)

chbx.setChecked(True)
chbx2 = QCheckBox(window, text='Android')
chbx2.setChecked(False)
chbx2.move(60,80)
chbx3 = QCheckBox('Hwawi',window)
chbx3.move(60,100)
chbx3.setChecked(True)

print (chbx3.isChecked())
window.show()
app.exec_()
