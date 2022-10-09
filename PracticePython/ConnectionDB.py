from time import sleep

import mysql.connector
from mysql.connector import Error


class ConnectionDB:

    countCall = 1
    db = None

    def GetData (self):
        self.StillToConnecting()
        print(self.db.is_connected())
        print("After get dta ")
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM tag')
        result = cursor.fetchall()
        for row in result:
            print(row)

        cursor.close()
        self.db.close()


    @staticmethod
    def Connectiong ():
        con = None
        try:
            con = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='',
                database='test')

            if(con.connect()):
                print("Succes Connecting", con.connect())
            else:
                print("Failed Connecting", con.connect())

        except Error as error:
            print(error)
            sleep(1)
            # self.Connectiong()


    def StillToConnecting(self):
        try:
            if self.db==None:
                self.db = mysql.connector.connect(host='localhost', user='root', passwd='', database='test')
            print("Success Connecting")
            #print(self.countCall)
            print("\n")
        except:
            print("No connection")
            sleep(1)
            self.StillToConnecting()
            self.countCall += 1


# print(ConnectionDB().StillToConnecting())
Obj_Class_Connection = ConnectionDB()
Obj_Class_Connection.GetData()

# print(ConnectionDB().ConnectingMysqlDataBase())

#ConnectionDB.Connectiong()

