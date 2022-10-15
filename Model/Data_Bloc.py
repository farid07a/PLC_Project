import mysql.connector
from PracticePython.ConnectionMysqlDB import ConnectionMysqlDB

class DataBlock:

    number_db = 0
    desc_db = ""
    size_db = 0
    value_db = bytearray()
    ID_PLC = 0
    connection_mysql = ConnectionMysqlDB()

    def __init__(self, number_db, desc_db, value_db,ID_PLC):
        self.number_db = number_db
        desc_db = "data_block_{ }"
        self.desc_db = desc_db.format(self.number_db)
        self.value_db = value_db
        self.ID_PLC=ID_PLC


    # setter  & getter
    def set_id(self,id_db):
        self.id_db= id_db

    def set_number_db(self,number_db):
        self.number_db=number_db

    def set_value_db(self,value_db):
        self.value_db=value_db

    def get_id(self):
        return self.id_db

    def get_number_db(self):
        return self.number_db

    def get_value_db(self):
        return self.value_db

    def Insert_data_block(self):
        query = "INSERT INTO (number_db,desc_db,value_db,ID_PLC) VALUES (%s,%s,%s,%s)"
        try:
            self.connection_mysql.connecting()
            cursor=self.connection_mysql.get_connection().cursor()
            tuple_data_block=(self.number_db,self.desc_db,self.value_db,self.ID_PLC)
            cursor.execute(query,tuple_data_block)
            print("data block Created Automatically in PLC ")
            self.connection_mysql.get_connection().commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            if self.connection_mysql.get_connection().is_connected():
                self.connection_mysql.get_connection().close
                cursor.close()
                print("MySQL connection is closed")

