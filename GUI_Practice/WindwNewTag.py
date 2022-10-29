import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QDesktopWidget, QPushButton, QTableWidget, QLabel, \
    QLineEdit, QComboBox, QTableWidgetItem


from Model.PLC import plcMachine
from Model.Tag import tag


class WindowNewTag(QWidget):
    tag_obj = None
    tab_tags = None
    txt_lin_name_tag = None
    ad_st_byte = None
    cmb_datatype = None
    plc = plcMachine("", "", 0, 1)

    def __init__(self):
        super().__init__()

        self.resize(800, 500)

        lab_name_tag = QLabel("N° PLC:", self)
        lab_name_tag.setGeometry(20, 0, 100, 35)

        self.cmb_plcs = QComboBox(self)
        self.cmb_plcs.setGeometry(125, 0, 150, 35)

        lab_name_tag = QLabel("Name Tag:", self)
        lab_name_tag.setGeometry(20, 50, 100, 35)

        self.txt_lin_name_tag = QLineEdit(self)
        self.txt_lin_name_tag.setPlaceholderText("Input tag name")
        self.txt_lin_name_tag.setGeometry(125, 50, 150, 35)

        lab_name_tag = QLabel("Data type tag:", self)
        lab_name_tag.setGeometry(20, 100, 100, 35)

        self.cmb_datatype = QComboBox(self)
        self.cmb_datatype.setGeometry(125, 100, 150, 35)
        self.cmb_datatype.addItem('bool')
        self.cmb_datatype.addItem('int')
        self.cmb_datatype.addItem('real')

        lab_name_tag = QLabel("Address start byte:", self)
        lab_name_tag.setGeometry(20, 150, 100, 35)

        self.ad_st_byte = QLineEdit(self)
        self.ad_st_byte.setPlaceholderText("Input start address byte")
        self.ad_st_byte.setGeometry(125, 150, 150, 35)
        self.ad_st_byte.textChanged.connect(self.control_address_)
        lab_ad_bit = QLabel("Address start bit:", self)
        lab_ad_bit.setGeometry(20, 200, 100, 35)

        self.ad_st_bit = QLineEdit(self)
        self.ad_st_bit.setPlaceholderText("Input start address bit")
        self.ad_st_bit.setGeometry(125, 200, 150, 35)
        self.ad_st_bit.setEnabled(True) # because first item in combo data_type is bool


        self.btn_save = QPushButton('Save', self)
        self.btn_save.setGeometry(200, 300, 80, 35)

        self.btn_cancel = QPushButton('Cancel', self)
        self.btn_cancel.setGeometry(90, 300, 80, 35)

        self.msg_to_user = QLabel("", self)
        self.msg_to_user.setGeometry(10, 360, 200, 35)
        self.msg_to_user.setStyleSheet('color:red')

        self.tab_tags = QTableWidget(self)
        self.tab_tags.resize(500, 200)
        self.tab_tags.move(300, 50)
        self.tab_tags.setRowCount(0)
        self.tab_tags.setColumnCount(4)
        self.tab_tags.setHorizontalHeaderLabels(["N°", "Name", "datatype", "Address"])
        # for i in range(0,3):
        #     self.tab_tags.setItem(i,0,QTableWidgetItem('1'))
        #     self.tab_tags.setItem(i, 1,QTableWidgetItem('1'))
        #     self.tab_tags.setItem(i, 2, QTableWidgetItem('1'))
        #     self.tab_tags.setItem(i,3, QTableWidgetItem('1'))

        self.load_tags()
        self.load_plcs_combobox()
        self.cmb_datatype.currentIndexChanged.connect(self.change_select_item_data_type)
        self.btn_save.clicked.connect(self.save_tag_in_database)

    def load_tags(self):
        self.tag_obj = tag()
        list_tags = self.tag_obj.list_of_tags()
        self.tab_tags.setRowCount(0)
        for i in range(0, len(list_tags)):
            print(list_tags[i].get_id_tag())
            self.tab_tags.insertRow(i)
            # self.tab_tags.setItem(i, 0, QTableWidgetItem('1'))
            # self.tab_tags.setItem(i, 1, QTableWidgetItem('2'))
            # self.tab_tags.setItem(i, 2, QTableWidgetItem('3'))
            # self.tab_tags.setItem(i, 3, QTableWidgetItem('4'))
            self.tab_tags.setItem(i, 0, QTableWidgetItem(str(list_tags[i].get_id_tag())))
            self.tab_tags.setItem(i, 1, QTableWidgetItem(str(list_tags[i].get_name_tag())))
            self.tab_tags.setItem(i, 2, QTableWidgetItem(str(list_tags[i].get_data_type())))

            address_bit = 0 if list_tags[i].get_address_start_byte() != "bool" else list_tags[i].get_address_start_bit()
            self.tab_tags.setItem(i, 3,
                                  QTableWidgetItem(str(list_tags[i].get_address_start_byte()) + "." + str(address_bit)))

    def save_tag_in_database(self):
        name = self.txt_lin_name_tag.text()
        data_type = self.cmb_datatype.currentText()
        addres_byte = self.ad_st_byte.text()
        addres_bit = -1
        if self.ad_st_bit.isEnabled():
            addres_bit = self.ad_st_bit.text()
        #  Name, Data_Type, Address_start_byte, Address_start_bit, ID_PLC
        id_plc = self.cmb_plcs.currentText()

        self.tag_obj.create_object(0, name, data_type, addres_byte, addres_bit, id_plc)
        self.tag_obj.insert_tag_in_database()
        self.load_tags()

    def load_plcs_combobox(self):
        tuple_plc = self.plc.get_list_plc()
        for plc in tuple_plc:
            self.cmb_plcs.addItem(str(plc[0]))

    def change_select_item_data_type(self):
        if self.cmb_datatype.currentText() == "bool":
            self.ad_st_bit.setEnabled(True)

        elif self.ad_st_bit.isEnabled():
            self.ad_st_bit.setEnabled(False)

    def control_address_(self):

        address_by_user = self.ad_st_byte.text()

        print("Input Address by user :",address_by_user)

        if address_by_user != "":

            print("Input text not empty")
            list_address = self.tag_obj.get_occupied_memory_cases()
            list_byte_occupied = list_address[0]
            print("list address reserved:", list_byte_occupied)
            address_by_user = int(address_by_user)
            print("Address to int :",address_by_user)

            if address_by_user in list_byte_occupied:
                print("Address is Reserved")
                self.btn_save.setEnabled(False)
                tag_name = self.tag_obj.get_tag_name_by_address(address_by_user)
                print("name of tag :: ", tag_name)
                self.msg_to_user.setStyleSheet('color: red')
                print("passed color")
                if tag_name !="":
                    self.msg_to_user.setText("this Address is reserved for :"+ tag_name)
            else:
                self.msg_to_user.setText("This Address is free ")
                self.msg_to_user.setStyleSheet('color: green')
                #self.msg_to_user.setFont(QFont('Arial', 13))

        else:
            print("Empty input text ")
            self.btn_save.setEnabled(True)
            self.msg_to_user.setText("No input address ")


# app = QApplication(sys.argv)
# print("pass app")
# WindowNewPLC_obj = WindowNewTag()
# WindowNewPLC_obj.show()
# #
# app.exec_()

#