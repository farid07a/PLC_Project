import mysql.connector
from mysql.connector import Error


class ConnectionDB:
    @staticmethod
    def ConnectingMysqlDataBase():
        try:
            db = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='',
                database='test'
            )
        except:
            print("No connection")


        print(db.is_connected())

        print("After get dta ")
        cursor = db.cursor()
        cursor.execute('SELECT * FROM tag')
        result = cursor.fetchall()
        for row in result:
            print(row)

        cursor.close()
        db.close()

print(ConnectionDB().ConnectingMysqlDataBase())

    def Connectiong():
        con= None
        try:
            con=mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='',
                database='test')

            if(con.connect()):
                print("Succes Connecting")
            else:
                print("Failed Connecting")

        except Error as error:
            print(error)