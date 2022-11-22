# simple list of integers
import sqlite3
from Model_Control_.ConnectionSqliteDB import ConnectionSqliteDB


class SplitDataPackage:
    ID_Tag = 0
    ID_Input =0
    Value_Tag = bytearray(0)

    connection_sqlite = ConnectionSqliteDB()

    def create(self,ID_Tag,ID_Input,Value_Tag):
        self.ID_Tag=ID_Tag
        self.ID_Input=ID_Input
        self.Value_Tag=Value_Tag

    def insert_split_data_package_database(self):
        query = "INSERT INTO tag_input(ID_Tag,ID_Input,Value_Tag) VALUES (?,?,?)"
        try:
            self.connection_sqlite.connecting()
            cursor = self.connection_sqlite.get_connection().cursor()
            split_data_tag = (self.ID_Tag, self.ID_Input, self.Value_Tag)
            print("Data To insert : ", split_data_tag)
            cursor.execute(query, split_data_tag)
            print("success Insert partition in table tag_input")
            self.connection_sqlite.get_connection().commit()
            cursor.close()
        except sqlite3.Error as error:
            print("Error insert_split_data_package_database:",error)
        finally:
            if self.connection_sqlite.get_connection():
                self.connection_sqlite.disconnect()






# list = [1,2]
# split_data_tag = SplitDataPackage()
# split_data_tag.create(1,1,bytearray(list))
# split_data_tag.insert_split_data_package_database()

#
# # iterable as source
# array = bytearray()
#
# print(array)
# print("Count of bytes:", len(array))
#
# #tuple having only integer type of data.
# a=(1,2,3,4)
# print(a) #prints the whole tuple
#
# #tuple having multiple type of data.
# b=("hello", 1,2,3,"go")
# print(b) #prints the whole tuple
#
# #index of tuples are also 0 based.
#
# print(b[4]) #this prints a single element in a tuple, in this case "go"
#
#
# b = bytes()
# floatList = [5.4, 3.5, 7.3, 6.8, 4.6]
# b = b.join((struct.pack('f', val) for val in floatList))
#
# by=bytearray(b)
# print(by)
#
# print(len(by))



