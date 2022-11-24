import sqlite3

from app import Connection
from app.Connection import ConnectionSqliteDB


class Tag:

    def __init__(self, ID_Tag, Name, Data_Type, Address_start_byte, Address_start_bit, ID_PLC):
        self.__ID_Tag = ID_Tag
        self.__Name = Name
        self.__Data_Type = Data_Type
        self.__Address_start_byte = Address_start_byte
        self.__Address_start_bit = Address_start_bit
        self.__ID_PLC = ID_PLC

    def get_id_tag(self):
        return self.__ID_Tag

    def get_name_tag(self):
        return self.__Name

    def get_data_type(self):
        return self.__Data_Type

    def get_address_start_byte(self):
        return self.__Address_start_byte

    def get_address_start_bit(self):
        return self.__Address_start_bit

    def get_id_plc(self):
        return self.__ID_PLC

    def set_id_tag(self, ID_Tag):
        self.__ID_Tag = ID_Tag

    def set_tag_name(self, Name):
        self.__Name = Name

    def set_tag_data_type(self, Data_Type):
        self.__Data_Type = Data_Type

    def set_tag_address_start_byte(self, Address_start_byte):
        self.__Address_start_byte = Address_start_byte

    def set_tag_address_start_bit(self, Address_start_bit):
        self.__Address_start_bit = Address_start_bit

    def set_id_plc(self, ID_PLC):
        self.__ID_PLC = ID_PLC

    def insert_tag_in_database(self):
        query = "INSERT INTO tag (Name,Data_Type,Address_start_byte,Address_start_bit,ID_PLC) " \
                "        VALUES (?  ,?       ,?                ,?               ,?)"
        try:
            ConnectionSqliteDB.connecting()
            val = (self.__Name, self.__Data_Type, self.__Address_start_byte, self.__Address_start_bit, self.__ID_PLC)
            cursor = ConnectionSqliteDB.get_connection().cursor()
            cursor.execute(query, val)
            ConnectionSqliteDB.get_connection().commit()
            print("Success Add Tag")
            cursor.close()
        except sqlite3.Error as error:
            print(error)
        finally:
            if ConnectionSqliteDB.get_connection():
                ConnectionSqliteDB.disconnect()

    @staticmethod
    def get_data_tags_in_database():
        query = "select * from tag"
        list_tag = []
        try:
            ConnectionSqliteDB.connecting()
            cursor = ConnectionSqliteDB.get_connection().cursor()
            cursor.execute(query)
            list_tag = cursor.fetchall()
            cursor.close()
        except sqlite3.Error as error:
            print(error)
        finally:
            if ConnectionSqliteDB.get_connection():
                ConnectionSqliteDB.disconnect()

        return list_tag


tag_obj=Tag(1,"tag_name","int",13,3,1)
tag_obj.insert_tag_in_database()
print(tag_obj.get_data_tags_in_database())
