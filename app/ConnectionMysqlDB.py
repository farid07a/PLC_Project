from time import sleep
import mysql.connector
from mysql.connector import Error
#from mysql.connector import CMySQLConnection

import sqlite3

import pyodbc
class ConnectionMysqlDB:

    __instance = None       # instance of class
    __connection_db = None  # attribute connection

    @classmethod
    def __init_constructor(cls): # return default constructor with class method
        return cls()

    @classmethod
    def get_instance(cls):
        if ConnectionMysqlDB.__instance is None:
            ConnectionMysqlDB.__instance = ConnectionMysqlDB.__init_constructor()  # test if object created

        return ConnectionMysqlDB.__instance


    def connecting(self):
        try:
            ConnectionMysqlDB.__connection_db = sqlite3.connect('D:\database_plc.db')
            print("success connecting")
        # When Error in connection has Occurred
        except sqlite3.Error as e:
            print(e)
    @classmethod
    def get_connection(cls):
        return ConnectionMysqlDB.__connection_db

    @classmethod
    def disconnect(cls):
        ConnectionMysqlDB.__connection_db.close()

obj_cnx = ConnectionMysqlDB.get_instance()

obj_cnx.connecting() #
print(obj_cnx)
print(ConnectionMysqlDB.get_connection())



obj_cnx1 = ConnectionMysqlDB.get_instance()
print(obj_cnx1)
print(ConnectionMysqlDB.get_connection())

obj_cnx.disconnect()

