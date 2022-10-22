from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
import sys
app = QApplication(sys.argv)
form = QWidget()
form.resize(600,600)
form.move(100,100)
re=QMessageBox.question(form,"confirmation","confirmation text",QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)

print("yes",re)

print(QMessageBox.question(form,"confirmation","confirmation text",QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes))

if re== QMessageBox.Yes:
    print(" yes ")
else:
    print("No")
# if re == 1:
#     re=QMessageBox.information(form,"confirmation","confirmation text",QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
# elif re==2:

form.show()

app.exec_()


