from time import sleep
import MySQLdb
import mysql.connector
from mysql.connector import Error
#from mysql.connector import CMySQLConnection

class ConnectionDB:

    def __init__(self):
        self.connection = mysql.connector.MySQLConnection()

    def get_data(self):
        self.connecting()
        print(self.connection.is_connected())
        print("After get dta ")
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM tag')
        result = cursor.fetchall()
        for row in result:
            print(row)
        cursor.close()
        self.connection.close()

    def connecting(self):

        try:
            if self.connection.is_connected():
                self.connection = mysql.connector.connect(host='localhost', user='root', passwd='', database='test')
            print("Success Connecting")
        except MySQLdb.Error as e:
            print("No connection")
            sleep(1)
            self.connecting()

    def get_connection(self):
        return self.connection

    def set_connection(self, connection):
        self.connection = connection

    def disconnect(self):
        self.connection.close()

print(ConnectionDB().connecting())
# Obj_Class_Connection = ConnectionDB()
# Obj_Class_Connection.GetData()

# print(ConnectionDB().ConnectingMysqlDataBase())

# ConnectionDB.Connectiong()
