import datetime
import sqlite3

from snap7.util import set_int, set_real, set_bool

from Model.ConnectionSqliteDB import ConnectionSqliteDB


class InputData:
    ID_Input = 0
    Data_Input = bytearray()
    Time_Input = None
    connection_sqlite = ConnectionSqliteDB()

    def create(self, ID_Input, Data_Input, Time_Input):
        self.ID_Input = ID_Input
        self.Data_Input = Data_Input
        self.Time_Input = Time_Input

    # insert byte_array of db (full data) in database with time read
    #
    def insert_input_data(self):
        query = "INSERT INTO input_table (Data_Input,Time_Input) VALUES (?,?)"
        try:
            self.connection_sqlite.connecting()
            cursor = self.connection_sqlite.get_connection().cursor()
            data_read = (self.Data_Input, datetime.datetime.now())
            cursor.execute(query, data_read)
            print("Success Insert Data input ")
            self.connection_sqlite.get_connection().commit()
            cursor.close()
        except sqlite3.Error as error:
            print(error)
        finally:
            if self.connection_sqlite.get_connection():
                self.connection_sqlite.disconnect()

    # get last_id of operation read data
    # return last last_id
    def get_last_operation_read(self):
        query = "SELECT MAX(ID_Input) FROM input_table"
        last_id = 0
        try:
            self.connection_sqlite.connecting()
            cursor = self.connection_sqlite.get_connection().cursor()
            cursor.execute(query)
            list_op = cursor.fetchall()
            # print(last_op)
            for i in list_op:
                last_id = i[0]
            cursor.close()
        except sqlite3.Error as error:
            print(error)
        finally:
            if self.connection_sqlite.get_connection():
                self.connection_sqlite.disconnect()
        return last_id

    # list tag_input
    def get_list_operation_tag_input_table(self):   # get list all
        query = "SELECT DISTINCT ID_Input FROM tag_input"
        list_id = []
        try:
            self.connection_sqlite.connecting()
            cursor = self.connection_sqlite.get_connection().cursor()
            cursor.execute(query)
            list_id = cursor.fetchall()
            cursor.close()
        except sqlite3.Error as error:
            print(error)
        finally:
            if self.connection_sqlite.get_connection():
                self.connection_sqlite.disconnect()
        return list_id

    # not testing with sqlite
    def get_list_operation_input_between_two_dates(self, dt1, dt2):
        query = "SELECT DISTINCT ID_Input FROM input_table  " \
                "WHERE  input_table.Time_Input >= ?  AND input_table.Time_Input <= ? "

        list_id = []
        try:
            self.connection_sqlite.connecting()
            cursor = self.connection_sqlite.get_connection().cursor()
            cursor.execute(query, (dt1, dt2))
            list_id = cursor.fetchall()
            cursor.close()
        except sqlite3.Error as error:
            print(error)
        finally:
            if self.connection_sqlite.get_connection():
                self.connection_sqlite.disconnect()
        return list_id

#
# db = bytearray(20)
# # #
# # set_int(db, 0, 300)
# set_real(db, 2, 55.5)
# set_bool(db, 6, 0, 1)
#
# set_bool(db, 6, 1, 0)
# set_real(db, 7, 12.51)
# # # set_bool(db, 11, 0, 1)
# # #
# # # print("db array :", db)
# ReadObj = InputData()
# # ReadObj.Data_Input = db
# # ReadObj.insert_input_data()
# print(ReadObj.get_last_operation_read())
