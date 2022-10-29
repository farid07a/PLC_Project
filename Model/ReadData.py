import datetime
import mysql.connector
from snap7.util import set_int, set_real, set_bool

from Model.ConnectionMysqlDB import ConnectionMysqlDB


class InputData:
    ID_Input = 0
    Data_Input = bytearray()
    Time_Input = None
    connection_mysql = ConnectionMysqlDB()

    def create(self, ID_Input, Data_Input, Time_Input):
        self.ID_Input = ID_Input
        self.Data_Input = Data_Input
        self.Time_Input = Time_Input

    def insert_input_data(self):
        query = "INSERT INTO input_table (Data_Input,Time_Input) VALUES (%s,%s)"
        cursor = None
        try:
            self.connection_mysql.connecting()
            cursor = self.connection_mysql.get_connection().cursor()
            data_read = (self.Data_Input, datetime.datetime.now())
            cursor.execute(query, data_read)
            print("Success Insert Data input ")
            self.connection_mysql.get_connection().commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            if self.connection_mysql.get_connection().is_connected():
                cursor.close()
                self.connection_mysql.disconnect()

    def get_last_operation_read(self):
        query = "SELECT MAX(ID_Input) FROM input_table"
        last_id = 0
        cursor = None
        try:
            self.connection_mysql.connecting()
            cursor = self.connection_mysql.get_connection().cursor()
            cursor.execute(query)
            list_op = cursor.fetchall()
            # print(last_op)
            for i in list_op:
                last_id = i[0]

        except mysql.connector.Error as error:
            print(error)
        finally:
            if self.connection_mysql.get_connection().is_connected():
                cursor.close()
                self.connection_mysql.disconnect()
        return last_id

    def get_list_operation_tag_input_table(self):   # get list all
        query = "SELECT DISTINCT ID_Input FROM tag_input"
        list_id = []
        cursor = None
        try:
            self.connection_mysql.connecting()
            cursor = self.connection_mysql.get_connection().cursor()
            cursor.execute(query)
            list_id = cursor.fetchall()

        except mysql.connector.Error as error:
            print(error)
        finally:
            if self.connection_mysql.get_connection().is_connected():
                cursor.close()
                self.connection_mysql.disconnect()
        return list_id

    def get_list_operation_input_between_two_dates(self,dt1,dt2):

        query = "SELECT DISTINCT ID_Input FROM input_table  " \
                "WHERE  input_table.Time_Input >= %s  AND input_table.Time_Input <= %s "

        list_id = []
        cursor = None
        try:
            self.connection_mysql.connecting()
            cursor = self.connection_mysql.get_connection().cursor()
            cursor.execute(query, (dt1, dt2))
            list_id = cursor.fetchall()

        except mysql.connector.Error as error:
            print(error)
        finally:
            if self.connection_mysql.get_connection().is_connected():
                cursor.close()
                self.connection_mysql.disconnect()
        return list_id

# db = bytearray(20)
#
# set_int(db, 0, 300)
# set_real(db, 2, 55.5)
# set_bool(db, 6, 0, 1)
# set_bool(db, 6, 1, 0)
# set_real(db, 7, 12.51)
# set_bool(db, 11, 0, 1)
#
# print("db array :", db)
#
# # ReadObj = InputData()
# # ReadObj.Data_Input = db
# # ReadObj.insert_input_data()
# # print(ReadObj.get_last_operation_read())
