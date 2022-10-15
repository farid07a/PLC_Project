from time import sleep
import MySQLdb
import mysql.connector
from mysql.connector import Error
#from mysql.connector import CMySQLConnection


class ConnectionMysqlDB:

    connection_db = mysql.connector.connect()

    def connecting(self):
        try:
            if not self.connection_db.is_connected():
                print("Var myf Connection : ", self.connection_db.is_connected())
                self.connection_db=mysql.connector.connect(host='localhost', user='root', passwd='', database='test')
                print("Success Connecting dataBase")
            else:
                print("Deja connecting")
        # When Error in connection has Occurred
        except BaseException as e:
            print(e)
            sleep(1)
            self.connecting()

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


    # def connecting(self):
    #
    #     try:
    #         if self.connection.is_connected():
    #             self.connection = mysql.connector.connect(host='localhost', user='root', passwd='', database='myf')
    #         print("Success Connecting")
    #     except MySQLdb.Error as e:
    #         print("No connection")
    #         sleep(1)
    #         self.connecting()

    def get_connection(self):
        return self.connection_db

    def set_connection(self, connection_db):
        self.connection_db = connection_db

    def disconnect(self):
        self.connection_db.close()

# obj_cnx=ConnectionMysqlDB()
# obj_cnx.connecting()
# statCon=obj_cnx.get_connection().is_connected()
# print(statCon)

# Obj_Class_Connection = ConnectionDB()
# Obj_Class_Connection.GetData()

# print(ConnectionDB().ConnectingMysqlDataBase())

# ConnectionDB.Connectiong()
