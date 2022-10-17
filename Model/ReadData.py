from datetime import datetime

import mysql.connector
from ConnectionMysqlDB import ConnectionMysqlDB
class InputData:

    ID_Input = 0
    Data_Input = bytearray()
    Time_Input = None

    connection_mysql = ConnectionMysqlDB()

    def create(self,ID_Input,Data_Input,Time_Input):
        self.ID_Input = ID_Input
        self.Data_Input=Data_Input
        self.Time_Input=Time_Input

    def insert_input_data(self):
        query = "INSERT INTO input_table (Data_Input,Time_Input) VALUES (%s,%s)"
        cursor = None
        try:
            self.connection_mysql.connecting()
            cursor = self.connection_mysql.get_connection().cursor()
            now = datetime.now()

            data_read = (self.Data_Input, now.strftime('%d-%m-%Y %H:%M:%S'))
            cursor.execute(query, data_read)
            print("Success Insert Data")
            self.connection_mysql.get_connection().commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            if self.connection_mysql.get_connection().is_connected():
                cursor.close()
                self.connection_mysql.disconnect()

    def get_last_operation_read(self):
        query="SELECT MAX(ID_Input) FROM input_table"
        last_op=0
        cursor=None
        try:
            self.connection_mysql.connecting()
            cursor = self.connection_mysql.get_connection().cursor()
            cursor.execute(query)
            last_op=cursor.fetchall()
            print(last_op)

        except mysql.connector.Error as error:
            print(error)
        finally:
            if self.connection_mysql.get_connection().is_connected():
                cursor.close()
                self.connection_mysql.disconnect()
        return last_op


ReadObj = InputData()
ReadObj.insert_input_data()
print(ReadObj.get_last_operation_read())

