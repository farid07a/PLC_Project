import sys
from PyQt5.QtWidgets import *
from connection import connect_db
import mysql.connector
from PyQt5.QtGui import QIcon
from new_interface import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("PLc_App")
        self.setWindowIcon(QIcon("Icons/plc.png"))

        tabl = self.ui.tableWidget
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(1, 60)
        self.ui.tableWidget.setColumnWidth(2, 70)
        #self.ui.tableWidget.setHorizontalHeaderLabels(["id", "name", "address", "test"])

        #self.loadDdata()

        self.ui.pushButton_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.pushButton_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.pushButton_8.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        self.ui.widget_4.setVisible(False)
        self.ui.widget_5.setVisible(False)
        self.ui.widget_8.setVisible(False)

        self.show()



    def loadDdata(self):
        cnx = mysql.connector.connect(host='localhost', user='root', passwd='Basma', port='3306', database='test',
                                      auth_plugin='mysql_native_password')
        curses = cnx.cursor()
        sql = ("SELECT * FROM plc")
        curses.execute(sql)
        rsult = curses.fetchall()

        print(rsult)
        indexrow = 0
        self.ui.tableWidget.setRowCount(len(rsult))
        for row in rsult:
            self.ui.tableWidget.setItem(indexrow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget.setItem(indexrow, 1, QtWidgets.QTableWidgetItem(row[1]))
            # self.tableWidget.setItem(indexrow, 2, QtWidgets.QTableWidgetItem(row[2]))
            indexrow += 1
            print(row)

    def remplirtable(self):
        print(" remplir table ..... ")
        c = connect_db()
        list = c.select_db("plc")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())