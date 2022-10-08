import mysql.connector
class ConnectionDB:

    def ConnectingMysqlDataBase(self):
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='test'
        )
        print(db)
        cursor = db.cursor()
        cursor.execute('SELECT * FROM tag')
        result = cursor.fetchall()
        for row in result:
            print(row)

        cursor.close()
        db.close()


print(ConnectionDB().ConnectingMysqlDataBase())

