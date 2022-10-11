import MySQLdb
from snap7 import client
import mysql.connector
from PracticePython import ConnectionDB
class plcMachine :

    connection_db = ConnectionDB.ConnectionDB()

    IdPlc = 0
    IP = ""
    RACK = 0
    SLOT = 1
    Status = True
    ModelPlc = ""
    clientPlc = client.Client()
    ConnectionObj=False

    def __init__(self,IdPlc, IP, RACK, SLOT ):
        self.IdPlc = IdPlc
        self.IP = IP
        self.RACK = RACK
        self.SLOT = SLOT

    def connecting(self):
        try:
            if not self.clientPlc.get_connected():
                self.clientPlc.connect(self.IP,self.RACK,self.SLOT)
                self.ConnectionObj = True
        except Exception as e:
            print(e)



    def connecting_To_PLC_Recursion(self):

        try:
            if self.ConnectionObj==False:
                self.clientPlc.connect(self.IP,self.RACK,self.SLOT)
                self.ConnectionObj=True
        except Exception as e:
            print("Occured Exception")

    def get_client_plc(self):
        return self.clientPlc

    def set_client_plc(self, clientPlc):
        self.clientPlc = clientPlc


    def setIdPlc(self,IdPlc):
        self.IdPlc = IdPlc

    def getIdPlc(self):
        return self.IdPlc

    def setIP(self,IP):
        self.IP = IP

    def getIP(self):
        return self.IP

    def setSolt(self,SLOT):
        self.SLOT=SLOT

    def getSlot(self):
        return self.SLOT

    def setRack(self,RACK):
        self.RACK=RACK

    def getRACK(self):
        return self.RACK

    def AddNewPLC(self):
        Query = "INSERT INTO plc_controller (Model,IP,RACK,	SLOT) values (%s,%s,%s,%s)"
        try:
            cnx=mysql.connector.connect()
            cursor = self.connection_db.get_connection().cursor()
            val = (self.ModelPlc,self.IP,self.RACK,self.SLOT)
            cursor.execute(Query, val)
            print("Success Insert Record")
            self.connection_db.get_connection().commit()
        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))
        finally:
            if self.connection_db.get_connection() is not None:
                cursor.close()
                self.connection_db.disconnect()
                print("MySQL connection is closed")

    def get_list_plc(self):
        query = "select * from plc_controller"
        cnx = None
        list_plc = []
        try:
            cnx = mysql.connector.connect(host='localhost', user='root', passwd='', database='test')
            cursor = cnx.cursor()
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
            cnx.close()

    def display_plc(self):
        list_plc = self.get_list_plc()
        size_row = list_plc[0].__len__()
        print("|id\t |Model\t |IP \t \t |Rack\t |SLOT\t|")
        for plc in list_plc:
            print("|", plc[0] ,"\t |", plc[1], "\t |", plc[2], "\t \t |",plc[3],"\t |",plc[4] ,"\t|")


    def menu(self):
        flag = True
        while flag:
            print(" Menu :\n 1: Add New PLC \n 2: Connecting To Plc \n 3 :Add Colum To Table PLC \n 4: Exit \n 5 display list plc")
            x = int(input(" Enter your Choice:\n"))
            if x == 1:
                self.AddNewPLC();
                # flag = False

            elif x == 2:
                self.connecting_To_PLC_Recursion()
            elif x == 3:
                print("Add New Colum In PLC Data")
                self.get_list_plc()
            elif x == 4:
                print("Close Menu")
                flag = False
            elif x== 5:
                self.display_plc()

obj= plcMachine("S7 1200", "172.16.5.100", 1, 0)
obj.menu()
