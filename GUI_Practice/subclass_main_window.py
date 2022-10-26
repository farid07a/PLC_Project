import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QDesktopWidget, QPushButton, QTableWidget, \
    QTableWidgetItem, QLabel, QLineEdit, QMenuBar, QMenu
from snap7 import client
from GUI_Practice.WindwNewTag import WindowNewTag
from GUI_Practice.form_history import history
from Model.PLC import plcMachine
from Model.ReadData import InputData
from Model.SplitDataPackage import SplitDataPackage


class MainWindow(QMainWindow):
    read_data_obj = InputData()
    split_data_tag = SplitDataPackage()
    plc_physic = client.Client()
    plc_object=None
    def __init__(self):
        super().__init__()

        self.tag_window=None
        self.history_window=None
        self.setWindowTitle("OOP GUI")
        #self.resize(600,600)
        self.setFixedSize(QSize(1000, 600)) # resizable not working
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.menu_bar=QMenuBar(self)

        self.new_menu = QMenu('new')
        self.connect_menu = QMenu('connect')
        self.menu_bar.addMenu(self.new_menu)
        self.menu_bar.addMenu(self.connect_menu)
        btn_plc = QPushButton('Connect PLC', self)
        btn_plc.move(50, 50)

        btn_history = QPushButton('Show history',self)
        btn_history.move(50,100)
        btn_history.clicked.connect(self.show_history_window)

        btn_tag = QPushButton('Add tag', self)
        btn_tag.move(50, 150)
        btn_tag.clicked.connect(self.show_tag_window)
        self.tab_plcs = QTableWidget(self)
        self.tab_plcs.resize(400,200)
        self.tab_plcs.move(150,50)
        #self.tab_plcs.setRowCount(3)

        self.tab_plcs.setColumnCount(4)
        self.tab_plcs.setHorizontalHeaderLabels(["N°","IP","RACK","SLOT"])

        lab_ip = QLabel("IP Address :", self)
        lab_ip.setGeometry(50, 350, 100, 35)

        self.txt_lin_ip = QLineEdit(self)
        self.txt_lin_ip.setPlaceholderText("IP Address")
        self.txt_lin_ip.setGeometry(125, 350, 150, 35)

        lab_RACK = QLabel("Rack :", self)
        lab_RACK.setGeometry(50, 400, 100, 35)

        self.txt_lin_rack = QLineEdit(self)
        self.txt_lin_rack.setPlaceholderText("RACK")
        self.txt_lin_rack.setGeometry(125, 400, 150, 35)

        lab_slot = QLabel("SLOT :", self)
        lab_slot.setGeometry(50, 450, 100, 35)

        self.txt_lin_slot = QLineEdit(self)
        self.txt_lin_slot.setPlaceholderText("SLOT")
        self.txt_lin_slot.setGeometry(125, 450, 150, 35)

        btn_sv_plc=QPushButton ('Save plc',self)
        btn_sv_plc.move(200,550)
        btn_sv_plc.clicked.connect(self.save_plc)
        btn_cnl_plc = QPushButton('cancel', self)
        btn_cnl_plc.move(0, 550)
        self.plc_object=plcMachine("","",0,1)
        self.load_plcs()

    def show_tag_window(self):
        self.tag_window = WindowNewTag()
        self.tag_window.show()

    def load_plcs(self):
        list_plcs = self.plc_object.get_list_plc()
        self.tab_plcs.setRowCount(0)
        size_list= len(list_plcs)
        for i in range(0,size_list):
            plc_info=list_plcs[i]
            print(plc_info)
            print(plc_info[0] , plc_info[1] ,plc_info[2] , plc_info[3] )
            self.tab_plcs.insertRow(i)
            self.tab_plcs.setItem(i,0,QTableWidgetItem(str(plc_info[0])))
            self.tab_plcs.setItem(i, 1, QTableWidgetItem(str(plc_info[1])))
            self.tab_plcs.setItem(i, 2, QTableWidgetItem(str(plc_info[2])))
            self.tab_plcs.setItem(i, 3, QTableWidgetItem(str(plc_info[3])))


    def show_history_window(self):
        self.history_window=history()
        self.history_window.show()

    def save_plc(self):
        rack = int(self.txt_lin_rack.text())
        slot = int(self.txt_lin_slot.text())
        self.plc_object = plcMachine(0, self.txt_lin_ip.text(), rack, slot)
        self.plc_object.insert_new_plc()
        self.load_plcs()


app = QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()