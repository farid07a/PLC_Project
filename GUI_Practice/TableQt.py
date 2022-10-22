from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QTableWidgetItem
import sys


def clic_table():
    for selctRow in my_table.selectedItems():
        print("Row :", selctRow.row()," col:",selctRow.column(), selctRow.text())


def double_click():
    for selctRow in my_table.selectedItems():
        print("Row :", selctRow.row()," col:",selctRow.column(), selctRow.text())


app = QApplication(sys.argv)
window = QWidget()
window.resize(700,500)
window.move(100,100)
my_table=QTableWidget(window)
my_table.setRowCount(2)
my_table.setColumnCount(3)
my_table.move(50,50)
my_table.resize(500,400)
my_table.setItem(0,0,QTableWidgetItem('00'))
my_table.setItem(0,1,QTableWidgetItem('01'))
my_table.setItem(0,2,QTableWidgetItem('02'))

my_table.setItem(1,0,QTableWidgetItem('01'))
my_table.setItem(1,1,QTableWidgetItem('01'))
my_table.setItem(1,2,QTableWidgetItem('02'))

my_table.setHorizontalHeaderLabels("ID:Name:Age".split(":"))
my_table.setVerticalHeaderLabels("a*b".split('*'))

# my_table.clicked.connect(clic_table)
my_table.doubleClicked.connect(double_click)

window.show()
app.exec_()

def cloc_table():
    for selctRow in my_table.selectedItems():
        print("Row :", selctRow.row()," col:",selctRow.column(), selctRow.text())

