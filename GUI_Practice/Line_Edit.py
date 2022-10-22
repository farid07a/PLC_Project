from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit
import sys

app = QApplication(sys.argv)
window = QWidget()

window.setGeometry(100,100,500,500)

btn = QPushButton ('click',window)

text_field= QLineEdit(window)
text_field.move(100,10)
text_field.resize(180,35)
text_field.setPlaceholderText("Enter tag Name")

text_field.setText("Tag 02")

# text_field.setEchoMode(QLineEdit.Password)

print(text_field.text())
text_field.setText(btn.text())
window.show()

app.exec_()
