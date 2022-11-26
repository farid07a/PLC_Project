import sys
from builtins import set

from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIcon
from connection import connect_db
import mysql.connector

from PyQt5.QtOpenGL import QGLWidget

class Gui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        uic.loadUi ('untitled.ui', self)

        self.setWindowTitle("PLc_App")
        self.setWindowIcon(QIcon("Icons/plc.png"))

        tabl=self.tableWidget
        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,60)
        self.tableWidget.setColumnWidth(2,70)
        self.tableWidget.setHorizontalHeaderLabels(["id","name","prenom","test" ])

        self.pushButton.clicked.connect(self.remplirtable)
        self.pushButton_3.clicked.connect(self.gettextfiled)
        self.pushButton_4.clicked.connect(self.clickbutton)

        self.loadDdata()

        self.pushButton_6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.pushButton_7.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.pushButton_8.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))


        self.widget_4.setVisible(False)
        self.widget_5.setVisible(False)
        self.widget_8.setVisible(False)

        self.show()
    def frameAffich(self):

       print()

    def loadDdata(self):
        cnx=mysql.connector.connect(host='localhost', user='root', passwd='Basma', port='3306', database='test',
                                       auth_plugin='mysql_native_password')
        curses=cnx.cursor()
        sql=("SELECT * FROM etudiant")
        curses.execute(sql)
        rsult = curses.fetchall()

        print(rsult)
        indexrow = 0
        self.tableWidget.setRowCount(len(rsult))
        for row in rsult:
            self.tableWidget.setItem(indexrow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(indexrow, 1, QtWidgets.QTableWidgetItem(row[1]))
            #self.tableWidget.setItem(indexrow, 2, QtWidgets.QTableWidgetItem(row[2]))
            indexrow+=1
            print(row)

    def remplirtable(self):
        print(" remplir table ..... ")
        c=connect_db()
        list=c.select_db("etudiant")

        for i in list:
                print("---------------:"+i[0] , i[1])


    def clickbutton(self):
        print("button clicked ....")


    def gettextfiled(self):
        print(self.lineEdit.text())
        #self.input = self.findChild(QtWidgets.QLineEdit, 'input')
        #self.input = self.findChild(QtWidgets.QLineEdit, 'input')


    def messagdialog(self):
        message=QtWidgets.QErrorMessage('yes','no','chose')

app = QtWidgets.QApplication(sys.argv)
frame = Gui()
sys.exit(app.exec_())
















