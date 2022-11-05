import datetime
import sqlite3

from Model_Control_.ConnectionSqliteDB import ConnectionSqliteDB


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
    def get_list_operation_tag_input_table(self,id_plc):   # get list all
        # query = "SELECT DISTINCT ID_Input FROM tag_input"
        query = "SELECT DISTINCT i.ID_Input FROM plc_controller p JOIN tag t ON p.ID_PLC= t.ID_PLC " \
              " JOIN tag_input ti ON ti.ID_Tag = t.ID_Tag " \
              " JOIN input_table i ON i.ID_Input=ti.ID_Input " \
              " WHERE p.ID_PLC = ?"
        list_id = []
        try:
            self.connection_sqlite.connecting()
            cursor = self.connection_sqlite.get_connection().cursor()
            cursor.execute(query, (id_plc,))
            list_id = cursor.fetchall()
            cursor.close()
        except sqlite3.Error as error:
            print(error)
        finally:
            if self.connection_sqlite.get_connection():
                self.connection_sqlite.disconnect()
        return list_id

    # not testing with sqlite
    def get_list_operation_input_between_two_dates(self, dt1, dt2, id_plc):
        query = "SELECT DISTINCT ID_Input FROM input_table  " \
                "WHERE  input_table.Time_Input >= ?  AND input_table.Time_Input <= ? "

        query = "SELECT DISTINCT i.ID_Input FROM plc_controller p JOIN tag t ON p.ID_PLC= t.ID_PLC " \
                " JOIN tag_input ti ON ti.ID_Tag = t.ID_Tag " \
                " JOIN input_table i ON i.ID_Input=ti.ID_Input " \
                " WHERE " \
                " (i.Time_Input >= ?  AND i.Time_Input <= ? ) " \
                " AND p.ID_PLC = ? "

        query = "SELECT DISTINCT i.ID_Input FROM plc_controller p " \
                "JOIN tag t ON p.ID_PLC= t.ID_PLC " \
                "JOIN tag_input ti ON ti.ID_Tag = t.ID_Tag " \
                "JOIN input_table i ON i.ID_Input=ti.ID_Input " \
                "WHERE (DATE(i.Time_Input) " \
                "BETWEEN  " \
                "date ('"+ "2022-11-02 13:45:35" + "') AND date ('" + "2022-11-02 14:45:35" + "')) " \
                " AND p.ID_PLC = 1"

        query = "SELECT DISTINCT i.ID_Input FROM plc_controller p " \
                "JOIN tag t ON p.ID_PLC= t.ID_PLC " \
                "JOIN tag_input ti ON ti.ID_Tag = t.ID_Tag " \
                "JOIN input_table i ON i.ID_Input=ti.ID_Input " \
                "WHERE (datetime(i.Time_Input) " \
                "BETWEEN  " \
                "datetime ('" + dt1 + "') AND datetime ('" + dt2 + "')) " \
                "AND p.ID_PLC = ?"

        list_id = []
        try:
            self.connection_sqlite.connecting()
            cursor = self.connection_sqlite.get_connection().cursor()
            cursor.execute(query, (id_plc,))
           # cursor.execute(query)
            list_id = cursor.fetchall()

            for row in list_id:
                print(row)

            cursor.close()
        except sqlite3.Error as error:
            print(error)
        finally:
            if self.connection_sqlite.get_connection():
                self.connection_sqlite.disconnect()
        return list_id





li = InputData().get_list_operation_input_between_two_dates("2022-11-02 10:45:35", "2022-11-02 14:45:35", 1)

print(li)
        # "2022-10-20 12:31:35", "2022-10-24 13:05:22"
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
