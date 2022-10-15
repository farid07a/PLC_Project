from time import sleep

import MySQLdb
from snap7 import client
import mysql.connector
from PracticePython import ConnectionMysqlDB
from PracticePython.ConnectionMysqlDB import ConnectionMysqlDB
from data_type import DataType


class plcMachine:
    # connection_db = ConnectionDB.ConnectionDB()
    IdPlc = 0
    IP = ""
    RACK = 1
    SLOT = 0
    # Status = True
    ModelPlc = "S7 1200"

    clientPlc = client.Client()
    ConnectionObj = False
    # var_connection = mysql.connector.connect()
    connection_mysql = ConnectionMysqlDB()

    # Constructor
    def __init__(self, IdPlc, IP, RACK, SLOT):
        self.IdPlc = IdPlc
        self.IP = IP
        self.RACK = RACK
        self.SLOT = SLOT

    # This Function for Connect Physic PLC
    def connecting_physique_plc(self):
        try:
            if not self.clientPlc.get_connected():
                self.clientPlc.connect(self.IP, self.RACK, self.SLOT)
                self.ConnectionObj = True
        except Exception as e:
            print(e)

    # Antagonistic Connection PLC
    def connecting_To_PLC_Recursion(self):
        try:
            if self.ConnectionObj == False:
                self.clientPlc.connect(self.IP, self.RACK, self.SLOT)
                self.ConnectionObj = True
        except Exception as e:
            print("Occurred Exception")

    # Setter & Getter Functions
    def get_client_plc(self):
        return self.clientPlc

    def set_client_plc(self, clientPlc):
        self.clientPlc = clientPlc

    def setIdPlc(self, IdPlc):
        self.IdPlc = IdPlc

    def getIdPlc(self):
        return self.IdPlc

    def setIP(self, IP):
        self.IP = IP

    def getIP(self):
        return self.IP

    def setSolt(self, SLOT):
        self.SLOT = SLOT

    def getSlot(self):
        return self.SLOT

    def setRack(self, RACK):
        self.RACK = RACK

    def getRACK(self):
        return self.RACK

    # Insert New PLC in DataBase
    def add_new_plc(self):
        Query = "INSERT INTO plc_controller (Model,IP,RACK,	SLOT) values (%s,%s,%s,%s)"
        try:
            self.test_connecttion()
            cursor = self.var_connection.cursor()
            val = (self.ModelPlc, self.IP, self.RACK, self.SLOT)
            cursor.execute(Query, val)
            print("Success Insert Record")
            self.var_connection.commit()
        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))
        finally:
            if self.var_connection.is_connected():
                cursor.close()
                self.var_connection.close()
                print("MySQL connection is closed")

    def Input_plc_informations(self):
        # self.connecting_physique_plc()
        var_connect_pysic_plc = True  # when PLC Connected we can insert
        if var_connect_pysic_plc:
            self.ModelPlc = input("Enter your PLC Model: ")
            self.setIP(input("Enter your IP Address: "))
            self.setRack(int(input("Enter Your PLC RACK: ")))
            self.setSolt(int(input("Input your Slot : ")))

    def insert_new_plc(self):  # Tested Pass
        query = "INSERT INTO plc_controller (Model,IP,RACK,	SLOT) values (%s,%s,%s,%s)"
        try:
            self.connection_mysql.connecting()
            cursor = self.connection_mysql.get_connection().cursor()
            tuple_proprites = (self.ModelPlc, self.IP, self.RACK, self.SLOT)
            cursor.execute(query, tuple_proprites)
            self.connection_mysql.get_connection().commit()
        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))
        finally:
            if self.connection_mysql.get_connection().is_connected():
                cursor.close()
                self.connection_mysql.get_connection().is_connected()
                print("MySQL connection is closed")

    def get_list_plc(self):  # Tested is passed
        query = "select * from plc_controller"
        list_plc = []
        try:
            self.connection_mysql.connecting()
            cursor = self.connection_mysql.get_connection().cursor()
            cursor.execute(query)
            print(cursor.column_names.__len__())
            list_plc = cursor.fetchall()

            for id in list_plc:
                print(id[0])
            cursor.close
            return list_plc
        except MySQLdb.Error as e:
            print(e)
        finally:
            self.connection_mysql.get_connection().close()

    def display_plc(self):  # tested pass
        list_plc = self.get_list_plc()
        size_row = list_plc[0].__len__()
        print("|id\t |Model\t |IP \t \t |Rack\t |SLOT\t|")
        for plc in list_plc:
            print("|", plc[0], "\t |", plc[1], "\t |", plc[2], "\t \t |", plc[3], "\t |", plc[4], "\t|")


    def add_new_colum_in_plc_table(self, name, value):
        datatype_obj = DataType()
        try:
            connection = mysql.connector.connect(user='root', passwd='', host='localhost', database='myf')
        except:
            print("Error: Can't connect to database")
            return
        dt_type = ''
        if type(value) == int:
            dt_type = datatype_obj.INT
        elif type(value) == float:
            dt_type = datatype_obj.FLOAT
        elif type(value) == str:
            dt_type = datatype_obj.VARCHAR
        elif type(value) == bool:
            dt_type = datatype_obj.BOOL
        elif type(value) == bytearray:
            dt_type = datatype_obj.BINARY
        else:
            print("Your value is not availble in my data_type class")
            return

        cursor = connection.cursor()
        sql = 'ALTER TABLE plc ADD COLUMN ' + name + ' ' + dt_type
        try:
            cursor.execute(sql)
            connection.commit()
        except:
            print("Error: unable to delete a record")
            connection.rollback()
        print(cursor.rowcount, 'record(s) deleted')
        cursor.close()
        connection.close()

    def menu(self):
        flag = True
        while flag:
            print(
                " Menu :\n 1: Add New PLC \n 2: Connecting To Plc \n 3 :Add Colum To Table PLC \n 4: Exit \n 5 display list plc")
            x = int(input(" Enter your Choice:\n"))
            if x == 1:
                self.Input_plc_informations()
                self.insert_new_plc();

                # flag = False

            elif x == 2:
                self.connecting_To_PLC_Recursion()
            elif x == 3:
                print("Add New Colum In PLC Data")
                self.get_list_plc()


            elif x == 4:
                print("Close Menu")
                flag = False
            elif x == 5:
                self.display_plc()


obj = plcMachine("S7 1200", "172.16.5.100", 0, 1)

obj.menu()


# table Local

# teg  int.2
# teg2 int.2
# teg3 0 4.0
# teg  4 4.1
# teg
