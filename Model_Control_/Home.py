import sys
import random
from time import sleep

import snap7
from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QDesktopWidget, QPushButton, QTableWidget, \
    QTableWidgetItem, QLabel, QLineEdit, QMenuBar, QMenu, QHeaderView, QMessageBox
from snap7 import client
from snap7.util import get_int, set_int, set_real, set_bool, get_real

from Model_Control_.Tag_Window import WindowNewTag
from Model_Control_.form_history import history
from Model_Control_.PLC import plcMachine
from Model_Control_.ReadData import InputData
from Model_Control_.SplitDataPackage import SplitDataPackage
from Model_Control_.Tag import tag


class Home(QMainWindow):
    read_data_obj = InputData()
    split_data_tag = SplitDataPackage()
    plc_physic = client.Client()
    plc_object = None
    stat_read_data = True

    def __init__(self):
        super().__init__()
        self.tag_window=None
        self.history_window=None
        self.setWindowTitle("OOP GUI")
        self.resize(1100,700)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        # self.setFixedSize(QSize(1100, 650)) # resizable not working
        # qtRectangle = self.frameGeometry()
        # centerPoint = QDesktopWidget().availableGeometry().center()
        # qtRectangle.moveCenter(centerPoint)
        # self.move(qtRectangle.topLeft())
        self.menu_bar = QMenuBar(self)

        self.new_menu = QMenu('new')
        self.connect_menu = QMenu('connect')
        self.menu_bar.addMenu(self.new_menu)
        self.menu_bar.addMenu(self.connect_menu)

        btn_plc = QPushButton('Connect PLC', self)
        btn_plc.move(10, 50)

        btn_history = QPushButton('Show history',self)
        btn_history.move(10,100)
        btn_history.clicked.connect(self.show_history_window)

        btn_tag = QPushButton('Add tag', self)
        btn_tag.move(10, 150)
        btn_tag.clicked.connect(self.show_tag_window)

        self.tab_plcs = QTableWidget(self)
        self.tab_plcs.resize(400,250)
        self.tab_plcs.move(140,50)
        #self.tab_plcs.setRowCount(3)

        self.tab_plcs.setColumnCount(4)
        self.tab_plcs.setHorizontalHeaderLabels(["N°","IP","RACK","SLOT"])

        self.tab_plcs.clicked.connect(self.get_plc_info_from_table)


        self.btn_reading_data = QPushButton('Start Reading',self)
        self.btn_reading_data.move(160, 330)
        self.btn_reading_data.clicked.connect(self.start_reading_data_plc)
        # self.btn_reading_data.clicked.connect(self.start_reading_data)

        self.btn_reading_data_manualy = QPushButton('test Reading Manualy', self)
        self.btn_reading_data_manualy.move(160, 370)
        self.btn_reading_data_manualy.clicked.connect(self.start_reading_data_without_while)
        # self.btn_reading_data.clicked.connect(self.start_reading_data)

        self.stop_reading_data = QPushButton('Stop reading', self)
        self.stop_reading_data.move(300, 330)
        self.stop_reading_data.clicked.connect(self.stop_reading)

        self.test_fill_table = QPushButton('testfill', self)
        self.test_fill_table.move(450, 330)
        self.test_fill_table.clicked.connect(self.table_test_fill)

        self.view_data_tags = QPushButton('View Data tags', self)
        self.view_data_tags.move(300, 370)
        self.view_data_tags.clicked.connect(self.prepare_table_tags_data)

        lab_ip = QLabel("IP Address :", self)
        lab_ip.setGeometry(10, 450, 100, 35)

        self.txt_lin_ip = QLineEdit(self)
        self.txt_lin_ip.setPlaceholderText("IP Address")
        self.txt_lin_ip.setGeometry(125, 450, 150, 35)

        lab_RACK = QLabel("Rack :", self)
        lab_RACK.setGeometry(10, 500, 100, 35)

        self.txt_lin_rack = QLineEdit(self)
        self.txt_lin_rack.setPlaceholderText("RACK")
        self.txt_lin_rack.setGeometry(125, 500, 150, 35)

        lab_slot = QLabel("SLOT :", self)
        lab_slot.setGeometry(10, 550, 100, 35)

        self.txt_lin_slot = QLineEdit(self)
        self.txt_lin_slot.setPlaceholderText("SLOT")
        self.txt_lin_slot.setGeometry(125, 550, 150, 35)

        self.btn_cnl_plc = QPushButton('cancel', self)
        self.btn_cnl_plc.move(100, 600)
        self.btn_cnl_plc.resize(80, 35)

        self.btn_sv_plc = QPushButton('Save plc', self)
        self.btn_sv_plc.move(200, 600)
        self.btn_sv_plc.resize(80, 35)

        self.btn_sv_plc.clicked.connect(self.save_plc)

        self.plc_object = plcMachine(0, "", 0, 1)
        self.load_plcs()
        # add New Table about reading data in form PLC

        self.tab_history = QTableWidget(self)
        self.tab_history.resize(700, 500)
        self.tab_history.move(550, 50)
        self.tag_obj = tag()

        # self.display_history_with_update_query()

    def table_test_fill(self):
        self.tab_history.setRowCount(0)

        self.prepare_table_view_data_reading_from_plc_horizontal_order()
        sleep(1)
        list_tags = self.tag_obj.list_of_tags_by_id_plc(self.plc_object.getIdPlc())  # get list of tags to get id
        i=0
        while i<10 :

            "===== read Date from Block Date type bool====="
            DB_NUMBER = 1  # The date block number to be read.
            START_ADDRESS = 0  # Starting Address Reading into Reading Block Date.
            # SIZE = self.tag_obj.get_size_db()  # Number of bytes to read from Date blocks.
            # print("Size Of data Block :", SIZE)

            # db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE) # REPLACE by test db byteArray

            db = bytearray(20)
            set_int(db, 0, random.randint(1, 100))
            set_real(db, 2, random.uniform(1.5, 17.9))
            set_bool(db, 6, 0, 0)
            set_bool(db, 6, 1, 1)
            set_real(db, 7, random.uniform(27.3, 40.8))

            print("db array :", db)

            self.read_data_obj.Data_Input = db  # set dataBloc to DataInput to save with operation
            print(self.read_data_obj.Data_Input)
            self.read_data_obj.insert_input_data()  # save The operation read of data with primary key
            id_read = self.read_data_obj.get_last_operation_read()  # return last id of Operation Read

            row_line = 0
            for tag_i in list_tags:
                id_tag = tag_i.get_id_tag()
                data_type = tag_i.get_data_type()
                addres_byte = tag_i.get_address_start_byte()
                print("ID_tag:", id_tag, "data_type:", data_type, "addres_byte:", addres_byte, "End_adres_byte",
                      addres_byte + 2)
                part_of_tag = bytearray()
                value = 0
                if data_type == "int":
                    part_of_tag = bytearray(2)
                    part_of_tag = db[addres_byte:addres_byte + 2]
                    print("part of package from db :", part_of_tag)
                    value = get_int(db, addres_byte)
                    print(get_int(db, addres_byte))
                elif data_type == "real":
                    part_of_tag = db[addres_byte:addres_byte + 4]
                    print(get_real(db, addres_byte))
                    value = get_real(db, addres_byte)
                    value = round(value, 1)

                elif data_type == "bool":
                    part_of_tag = bytearray(1)
                    addres_bit = tag_i.get_address_start_bit()
                    part_of_tag = db[addres_byte:addres_byte + 1]
                    print(snap7.util.get_bool(db, addres_byte, addres_bit))
                    value = snap7.util.get_bool(db, addres_byte, addres_bit)

                print("Last ID of Operation read :", id_read)
                self.split_data_tag.create(id_tag, id_read, part_of_tag)  #
                self.split_data_tag.insert_split_data_package_database()  # insert data in database
                # ---------------------------------------------------------------
                #self.tab_history.setItem(row_line, index_col, QTableWidgetItem(str(value)))  # correct
                self.tab_history.setItem(row_line, 4, QTableWidgetItem(str(value))) # incorrect
                row_line += 1
            i += 1

            sleep(1)

    def prepare_table_view_data_reading_from_plc_horizontal_order(self):
        self.tab_history.setRowCount(0)
        self.tab_history.resize(700, 500)
        self.tab_history.move(550, 50)
        self.tab_history.setColumnCount(5)
        self.tab_history.setHorizontalHeaderLabels(["N°", "Name", "datatype", "Address", "Value"])
        list_tags = self.tag_obj.list_of_tags_by_id_plc(self.plc_object.getIdPlc())
        print(list_tags)
        for i in range(0, len(list_tags)):
            print("*************************")
            print(list_tags[i].get_id_tag())
            self.tab_history.insertRow(i)
            self.tab_history.setItem(i, 0, QTableWidgetItem(str(list_tags[i].get_id_tag())))
            self.tab_history.setItem(i, 1, QTableWidgetItem(str(list_tags[i].get_name_tag())))
            self.tab_history.setItem(i, 2, QTableWidgetItem(str(list_tags[i].get_data_type())))
            address_bit = 0 if list_tags[i].get_address_start_byte() != "bool" else list_tags[i].get_address_start_bit()
            self.tab_history.setItem(i, 3, QTableWidgetItem(
                str(list_tags[i].get_address_start_byte()) + "." + str(address_bit)))
            self.tab_history.setItem(i, 4, QTableWidgetItem("00"))

        # showing data verticals
    def prepare_table_view_data_reading_from_plc_vertical_order(self):
        self.tab_history.setRowCount(0)
        print(self.plc_object.getIdPlc())
        sizeoflist = self.tag_obj.list_of_tags_by_id_plc(self.plc_object.getIdPlc())
        print("size of list is ",len(sizeoflist))
        self.tab_history.setColumnCount(len(sizeoflist) + 2)  # 2 = 1+1 (field time & id_plc)
        header = []
        header = self.tag_obj.list_names_of_tags_by_id_plc(self.plc_object.getIdPlc())
        header.append("time")
        header.append("N° plc")
        self.tab_history.setHorizontalHeaderLabels(header)
        self.tab_history.setColumnWidth(len(self.tag_obj.list_of_tags_by_id_plc(self.plc_object.getIdPlc())) + 1, 20)
        header = self.tab_history.horizontalHeader()
        header.setSectionResizeMode(5, QHeaderView.Stretch)


    def prepare_table_tags_data(self):
        print("enter in function ")
        self.prepare_table_view_data_reading_from_plc_horizontal_order()
        list_tags = self.tag_obj.list_of_tags_by_id_plc(self.plc_object.getIdPlc())
        ii=0
        try:
            self.plc_physic.connect(self.plc_object.getIP(), self.plc_object.getRACK(), self.plc_object.getSlot())
        except :
            print("error connecting physic plc")

        while ii<20 :
            db = bytearray(20)
            set_int(db, 0, random.randint(1, 100))
            set_real(db, 2, random.uniform(1.5, 17.9))
            set_bool(db, 6, 0, 0)
            set_bool(db, 6, 1, 1)
            set_real(db, 7, random.uniform(27.3, 40.8))

            self.read_data_obj.Data_Input = db  # set dataBloc to DataInput to save with operation
            print(self.read_data_obj.Data_Input)
            self.read_data_obj.insert_input_data()  # save The operation read of data with primary key
            id_read = self.read_data_obj.get_last_operation_read()  # return last id of Operation Read
            # get list of tags to get id

            row_line=0
            # self.tab_history.insertRow(row_line)
            for tag_i in list_tags:

                print("row :", row_line)
                # ------------------------------------------------------------------------
                id_tag = tag_i.get_id_tag()
                data_type = tag_i.get_data_type()
                addres_byte = tag_i.get_address_start_byte()
                print("ID_tag:", id_tag, "data_type:", data_type, "addres_byte:", addres_byte, "End_adres_byte",
                      addres_byte + 2)
                part_of_tag = bytearray(4)
                value = 0
                if data_type == "int":
                    part_of_tag = bytearray(2)
                    part_of_tag = db[addres_byte:addres_byte + 2]
                    print("part of package from db :", part_of_tag)
                    value = get_int(db, addres_byte)
                    print(get_int(db, addres_byte))
                elif data_type == "real":

                    part_of_tag = db[addres_byte:addres_byte + 4]
                    print(get_real(db, addres_byte))
                    value = get_real(db, addres_byte)
                    value = round(value, 1)

                elif data_type == "bool":
                    part_of_tag = bytearray(1)
                    addres_bit = tag_i.get_address_start_bit()
                    part_of_tag = db[addres_byte:addres_byte + 1]
                    print(snap7.util.get_bool(db, addres_byte, addres_bit))
                    value = snap7.util.get_bool(db, addres_byte, addres_bit)

                print("Last ID of Operation read :", id_read)
                self.split_data_tag.create(id_tag, id_read, part_of_tag)  #
                self.split_data_tag.insert_split_data_package_database()  # insert data in database
                # ---------------------------------------------------------------
                self.tab_history.setItem(row_line, 4, QTableWidgetItem(str(value)))  # correct
                row_line+=1

            ii+=1

        # for j in range(0, 100):
        #     print("inner loop ")
        #     val=random.randint(1, 100)
        #     i = random.randint(1, 4)
        #     self.tab_history.setItem(i, 4, QTableWidgetItem(str(val)))
        #     sleep(0.5)

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
        self.history_window=history(1)
        self.history_window.show()

    def save_plc(self):
        rack = int(self.txt_lin_rack.text())
        slot = int(self.txt_lin_slot.text())
        self.plc_object = plcMachine(0, self.txt_lin_ip.text(), rack, slot)
        self.plc_object.insert_new_plc()
        self.load_plcs()


    def display_history_with_update_query(self):
        #self.tab_history.setRowCount(0)

        list_operation_in_tag_input = InputData().get_list_operation_tag_input_table(self.plc_object.getIdPlc())  # get list of operations
        print("the operations operation ids= ", list_operation_in_tag_input)
        size_op_in_tag_input = len(list_operation_in_tag_input)
        print("size of list operation in table tag_input ", len(list_operation_in_tag_input))

        for i in range(0, size_op_in_tag_input):
            id_op_var = list_operation_in_tag_input[i] # array of tuple id operation
            print("id_op :", id_op_var[0])
            list_tags_by_id_operation = self.tag_obj.get_all_tags_and_time_optimized(id_op_var[0]) # retutn list
            print("Nbr tags related by operation N ", id_op_var[0], " = ", len(list_tags_by_id_operation))
            number_tag = len(list_tags_by_id_operation)
            self.tab_history.insertRow(i)
            time_read = ""
            plc_id = ""
            for j in range(0, len(list_tags_by_id_operation)):

                print("-- itr -- operation", i+1, " tag N :", j+1)

                tupele_id_op = list_tags_by_id_operation[j]

                print(tupele_id_op[0], " - ", tupele_id_op[1], " - ", tupele_id_op[2], " - ", tupele_id_op[3], " - ",
                      tupele_id_op[4], " - ", tupele_id_op[5], " - ", tupele_id_op[6])
                id_op = tupele_id_op[0]
                name_tag = tupele_id_op[1]
                data_type = tupele_id_op[2]
                value = 0
                if data_type == "int":
                    # value = get_int(tupele_id_op[4], 0)
                    value = int.from_bytes(tupele_id_op[4], 'big')
                elif data_type == "real":
                    value = snap7.util.get_real(tupele_id_op[4], 0)
                    value = round(value, 1)
                elif data_type == "bool":
                    ad_bit = tupele_id_op[3]
                    value = snap7.util.get_bool(tupele_id_op[4], 0, ad_bit)
                # ad_bit = tupele_id_op[3]
                # value=tupele_id_op[4]
                time_read = str(tupele_id_op[5])
                # print("Time Read :",time_read)
                plc_id = str(tupele_id_op[6])
                print(tupele_id_op[0]," - ",tupele_id_op[1]," - ", tupele_id_op[2]," - ",tupele_id_op[3], " - ", tupele_id_op[4], " - ", tupele_id_op[5], " - ",tupele_id_op[6])
                self.tab_history.setItem(i, j, QTableWidgetItem(str(value)))

            self.tab_history.setItem(i, len(list_tags_by_id_operation), QTableWidgetItem(time_read))
            self.tab_history.setItem(i, len(list_tags_by_id_operation) + 1, QTableWidgetItem(plc_id))

    def display_history_with_time_plc(self):
        self.tab_history.setRowCount(0)
        list_operation_in_tag_input = InputData().get_list_operation_tag_input_table(self.plc_object.getIdPlc())  # get list of operations

        print("the operations operation ids= ", list_operation_in_tag_input)
        size_op_in_tag_input = len(list_operation_in_tag_input)
        print("size of list operation in table tag_input ", len(list_operation_in_tag_input))

        for i in range(0, size_op_in_tag_input):
            id_op_var = list_operation_in_tag_input[i] # array of tuple id operation
            print("id_op :", id_op_var[0])
            list_tags_by_id_operation = self.tag_obj.get_all_tags_and_time_optimized(id_op_var[0]) # retutn list
            print("Nbr tags related by operation N ", id_op_var[0], " = ", len(list_tags_by_id_operation))
            number_tag = len(list_tags_by_id_operation)
            self.tab_history.insertRow(i)
            time_read = ""
            plc_id = ""
            for j in range(0, len(list_tags_by_id_operation)):
                print("-- itr -- operation", i+1, " tag N :", j+1)
                tupele_id_op = list_tags_by_id_operation[j]
                print(tupele_id_op[0], " - ", tupele_id_op[1], " - ", tupele_id_op[2], " - ", tupele_id_op[3], " - ",
                      tupele_id_op[4], " - ", tupele_id_op[5], " - ", tupele_id_op[6])
                id_op = tupele_id_op[0]
                name_tag = tupele_id_op[1]
                data_type = tupele_id_op[2]
                value = 0
                if data_type == "int":
                    #value = get_int(tupele_id_op[4], 0)
                    value = int.from_bytes(tupele_id_op[4], 'big')
                elif data_type == "real":
                    value = snap7.util.get_real(tupele_id_op[4], 0)
                elif data_type == "bool":
                    ad_bit = tupele_id_op[3]
                    value = snap7.util.get_bool(tupele_id_op[4], 0, ad_bit)

                # ad_bit = tupele_id_op[3]
                # value=tupele_id_op[4]
                time_read = str(tupele_id_op[5])
                # print("Time Read :",time_read)
                plc_id = str(tupele_id_op[6])
                print(tupele_id_op[0]," - ",tupele_id_op[1]," - ", tupele_id_op[2]," - ",tupele_id_op[3], " - ", tupele_id_op[4], " - ", tupele_id_op[5], " - ",tupele_id_op[6])
                self.tab_history.setItem(i, j, QTableWidgetItem(str(round(value, 1))))

            self.tab_history.setItem(i, len(list_tags_by_id_operation), QTableWidgetItem(time_read))
            self.tab_history.setItem(i, len(list_tags_by_id_operation) + 1, QTableWidgetItem(plc_id))


    def get_plc_info_from_table(self):
        for info in self.tab_plcs.selectedItems():
            print(info.row(), info.column(), info.text())
            print(self.tab_plcs.item(0, 0).text(), self.tab_plcs.item(0, 1).text(),
                  self.tab_plcs.item(0, 2).text(), self.tab_plcs.item(0, 3).text())

            self.plc_object = plcMachine(int(self.tab_plcs.item(info.row(), 0).text()),
                                         self.tab_plcs.item(info.row(), 1).text(),
                                          int(self.tab_plcs.item(info.row(), 2).text()),
                                          int(self.tab_plcs.item(info.row(), 3).text()))

            print(self.plc_object.getIdPlc(), " ", self.plc_object.getIP(), " ", self.plc_object.getRACK(),
                  self.plc_object.getSlot())

    def start_reading_data(self):
        self.tab_history.setRowCount(0)

        try:
            self.plc_physic.connect(self.plc_object.getIP(), self.plc_object.getRACK(), self.plc_object.getSlot())
        except:
            print("pass connection physic plc ")
        ii=0

        list_tags = self.tag_obj.list_of_tags_by_id_plc(self.plc_object.getIdPlc())
        self.tab_history.insertRow(1000)

        while True and ii <100:
            row_line = 0
            "===== read Date from Block Date type bool====="
            DB_NUMBER = 1  # The date block number to be read.
            START_ADDRESS = 0  # Starting Address Reading into Reading Block Date.
            # SIZE = self.tag_obj.get_size_db()  # Number of bytes to read from Date blocks.
            # print("Size Of data Block :", SIZE)

            # db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE) # REPLACE by test db byteArray

            db = bytearray(20)
            set_int(db, 0, random.randint(1, 100))
            set_real(db, 2, random.uniform(1.5, 17.9))
            set_bool(db, 6, 0, 0)
            set_bool(db, 6, 1, 1)
            set_real(db, 7, random.uniform(27.3, 40.8))

            print("db array :", db)

            self.read_data_obj.Data_Input = db  # set dataBloc to DataInput to save with operation
            print(self.read_data_obj.Data_Input)
            self.read_data_obj.insert_input_data()  # save The operation read of data with primary key
            id_read = self.read_data_obj.get_last_operation_read()  # return last id of Operation Read
              # get list of tags to get id
            index_col = 0
            # self.tab_history.insertRow(row_line)

            for tag_i in list_tags:

                print("row :",row_line," col:",index_col)
                #------------------------------------------------------------------------

                id_tag = tag_i.get_id_tag()
                data_type = tag_i.get_data_type()
                addres_byte = tag_i.get_address_start_byte()
                print("ID_tag:", id_tag, "data_type:", data_type, "addres_byte:", addres_byte, "End_adres_byte",
                      addres_byte + 2)
                part_of_tag = bytearray(4)
                value = 0
                if data_type == "int":
                    part_of_tag = bytearray(2)
                    part_of_tag = db[addres_byte:addres_byte + 2]
                    print("part of package from db :", part_of_tag)
                    value = get_int(db, addres_byte)
                    print(get_int(db, addres_byte))
                elif data_type == "real":
                    part_of_tag = db[addres_byte:addres_byte + 4]
                    print(get_real(db, addres_byte))
                    value = get_real(db, addres_byte)
                    value = round(value, 1)

                elif data_type == "bool":
                    part_of_tag = bytearray(1)
                    addres_bit = tag_i.get_address_start_bit()
                    part_of_tag = db[addres_byte:addres_byte + 1]
                    print(snap7.util.get_bool(db, addres_byte, addres_bit))
                    value = snap7.util.get_bool(db, addres_byte, addres_bit)

                print("Last ID of Operation read :", id_read)
                self.split_data_tag.create(id_tag, id_read, part_of_tag)  #
                self.split_data_tag.insert_split_data_package_database()  # insert data in database
                #---------------------------------------------------------------
                self.tab_history.setItem(row_line, index_col, QTableWidgetItem(str(value))) # correct
                # self.tab_history.setItem(row_line, index_col, QTableWidgetItem(str("value"))) # incorrect
                index_col += 1
                # self.display_history_with_update_query()
            row_line += 1


            #sleep(10)

    def start_reading_data_without_while(self):

        print(self.plc_object.getIdPlc())
        if self.plc_object.getIdPlc() > 0:
            self.prepare_table_view_data_reading_from_plc_vertical_order()
            try:
                self.plc_physic.connect(self.plc_object.getIP(), self.plc_object.getRACK(), self.plc_object.getSlot())
            except:
                print("pass connection physic plc ")

            "===== read Date from Block Date type bool====="
            DB_NUMBER = 1  # The date block number to be read.
            START_ADDRESS = 0  # Starting Address Reading into Reading Block Date.
            SIZE = self.tag_obj.get_size_db()  # Number of bytes to read from Date blocks.
            print("Size Of data Block :", SIZE)

            # db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE) # REPLACE by test db byteArray

            db = bytearray(20)

            set_int(db, 0, random.randint(1, 100))
            set_real(db, 2, random.uniform(1.5, 17.9))
            set_bool(db, 6, 0, 0)
            set_bool(db, 6, 1, 1)
            set_real(db, 7, random.uniform(27.3, 40.8))

            print("db array :", db)

            self.read_data_obj.Data_Input = db  # set dataBloc to DataInput to save with operation
            print(self.read_data_obj.Data_Input)
            self.read_data_obj.insert_input_data()  # save The operation read of data with primary key
            list_tags = self.tag_obj.list_of_tags_by_id_plc(self.plc_object.getIdPlc())  # get list of tags to get id
            for tag_i in list_tags:
                id_tag = tag_i.get_id_tag()
                data_type = tag_i.get_data_type()
                addres_byte = tag_i.get_address_start_byte()

                print("ID_tag:", id_tag, "data_type:", data_type, "addres_byte:", addres_byte, "End_adres_byte",
                      addres_byte + 2)
                part_of_tag = bytearray(4)

                if data_type == "int":
                    part_of_tag = db[addres_byte:addres_byte + 2]
                    print("part of package from db :", part_of_tag)
                    print(get_int(db, addres_byte))

                elif data_type == "real":
                    part_of_tag = db[addres_byte:addres_byte + 4]
                    print(get_real(db, addres_byte))

                elif data_type == "bool":
                    addres_bit = tag_i.get_address_start_bit()
                    part_of_tag = db[addres_byte:addres_byte + 1]
                    print(snap7.util.get_bool(db, addres_byte, addres_bit))

                id_read = self.read_data_obj.get_last_operation_read()  # return last id of Operation Read
                print("Last ID of Operationread :", id_read)
                self.split_data_tag.create(id_tag, id_read, part_of_tag)  #
                self.split_data_tag.insert_split_data_package_database()  # insert data in database

                #self.display_history_with_update_query()
                self.display_history_with_time_plc()
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle('Information')
            msg_box.setText("please select plc")
            msg_box.exec()

    def start_reading_data_plc(self):

        if (self.plc_object.getIdPlc()>0):
            try:
                self.plc_physic.connect(self.plc_object.getIP(), self.plc_object.getRACK(), self.plc_object.getSlot())
            except:
                print("pass connection physic plc ")
            list_tags = self.tag_obj.list_of_tags_by_id_plc(self.plc_object.getIdPlc())
            self.prepare_table_view_data_reading_from_plc_horizontal_order()
            while self.plc_physic.get_connected():

                "===== read Date from Block Date type bool====="
                DB_NUMBER = 1  # The date block number to be read.
                START_ADDRESS = 0  # Starting Address Reading into Reading Block Date.
                SIZE = self.tag_obj.get_size_db()  # Number of bytes to read from Date blocks.
                db = self.plc_physic.db_read(DB_NUMBER, START_ADDRESS, SIZE) # REPLACE by test db byteArray
                self.read_data_obj.Data_Input = db  # set dataBloc to DataInput to save with operation
                self.read_data_obj.insert_input_data()  # save The operation read of data with primary key
                id_read = self.read_data_obj.get_last_operation_read()  # return last id of Operation Read
                row_line = 0

                for tag_i in list_tags:
                    id_tag = tag_i.get_id_tag()
                    data_type = tag_i.get_data_type()
                    addres_byte = tag_i.get_address_start_byte()
                    value = 0
                    part_of_tag = bytearray()
                    if data_type == "int":
                        # part_of_tag = bytearray(2)
                        part_of_tag = db[addres_byte:addres_byte + 2]
                        value = get_int(db, addres_byte)

                    elif data_type == "real":
                        # part_of_tag = bytearray(4)
                        part_of_tag = db[addres_byte:addres_byte + 4]
                        value = get_real(db, addres_byte)
                        value = round(value, 1)

                    elif data_type == "bool":
                        # part_of_tag = bytearray(1)
                        addres_bit = tag_i.get_address_start_bit()
                        part_of_tag = db[addres_byte:addres_byte + 1]
                        value = snap7.util.get_bool(db, addres_byte, addres_bit)

                    self.split_data_tag.create(id_tag, id_read, part_of_tag)  #
                    self.split_data_tag.insert_split_data_package_database()  # insert data in database
                    self.tab_history.setItem(row_line, 4, QTableWidgetItem(str(value))) # correct
                    row_line += 1  # increment in [0- 4]
                sleep(0.5)
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle('Information')
            msg_box.setText("please select one plc")
            msg_box.exec()



    def stop_reading(self):
        self.stat_read_data=False

    def clear_data_in_plc(self):
        query =""



app = QApplication(sys.argv)
window=Home()
window.show()
app.exec_()