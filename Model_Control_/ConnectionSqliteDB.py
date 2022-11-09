from time import sleep
import mysql.connector
from mysql.connector import Error
#from mysql.connector import CMySQLConnection

import sqlite3

import pyodbc
class ConnectionSqliteDB:

    connection_db = sqlite3.connect('')

    # def connecting(self):
    #     try:
    #         if not self.connection_db.is_connected():
    #             # print("Var myf Connection : ", self.connection_db.is_connected())
    #             self.connection_db = mysql.connector.connect(host='localhost', user='root', passwd='', database= 'database_plc')
    #             # print("Success Connecting dataBase")
    #         else:
    #             print("Deja connecting")
    #     # When Error in connection has Occurred
    #     except BaseException as e:
    #         print(e)
    #         sleep(1)
    #         self.connecting()

    # def connecting(self):
    #     try:
    #         if not self.connection_db.is_connected():
    #             # print("Var myf Connection : ", self.connection_db.is_connected())
    #             self.connection_db = pyodbc.connect('Driver={SQL Server};' 'Server=SOFT\SQLEXPRESS;' 'Database=database_plc;'
    #                   'Trusted_Connection=yes;')
    #             print("success connecting")
    #         else:
    #             print("Deja connecting")
    #     # When Error in connection has Occurred
    #     except BaseException as e:
    #         print(e)
    #         sleep(1)
    #         self.connecting()

    # Connect to SQLLite

    def connecting(self):
        try:
            self.connection_db = sqlite3.connect('E:\database_plc.db')
            #self.connection_db = sqlite3.connect('database_plc_old.db')
            #self.connection_db = sqlite3.connect('\\Model_Control_\\database_plc.db')
            print("success connecting")
        # When Error in connection has Occurred
        except BaseException as e:
            print(e)
            sleep(1)
            self.connecting()


    def get_connection(self):
        return self.connection_db

    def set_connection(self, connection_db):
        self.connection_db = connection_db

    def disconnect(self):
        self.connection_db.close()

obj_cnx = ConnectionSqliteDB()
obj_cnx.connecting()
obj_cnx.disconnect()


# statCon=obj_cnx.get_connection().is_connected()
# print(statCon)

# Obj_Class_Connection = ConnectionDB()
# Obj_Class_Connection.GetData()

# print(ConnectionDB().ConnectingMysqlDataBase())

# ConnectionDB.Connectiong()
