import struct

# simple list of integers
from snap7.util import get_real
import mysql.connector
from Model.ConnectionMysqlDB import ConnectionMysqlDB


class SplitDataPackage:
    ID_Tag = 0
    ID_Input =0
    Value_Tag = bytearray()

    connection_mysql = ConnectionMysqlDB()

    def create(self,ID_Tag,ID_Input,Value_Tag):
        self.ID_Tag=ID_Tag
        self.ID_Input=ID_Input
        self.Value_Tag=Value_Tag

    def insert_split_data_package_database(self):
        query = "INSERT INTO tag_input(ID_Tag,ID_Input,Value_Tag) VALUES (%s,%s,%s)"
        cursor = None
        try:
            self.connection_mysql.connecting()
            cursor = self.connection_mysql.get_connection().cursor()
            split_data_tag = (self.ID_Tag,self.ID_Input,self.Value_Tag)
            cursor.execute(query, split_data_tag)
            print("success Insert partition in table tag_input")
            self.connection_mysql.get_connection().commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            if self.connection_mysql.get_connection().is_connected():
                cursor.close()
                self.connection_mysql.disconnect()

list = [1.5, 2.5, 0.54, 47.5]

# iterable as source
array = bytearray()

print(array)
print("Count of bytes:", len(array))

#tuple having only integer type of data.
a=(1,2,3,4)
print(a) #prints the whole tuple

#tuple having multiple type of data.
b=("hello", 1,2,3,"go")
print(b) #prints the whole tuple

#index of tuples are also 0 based.

print(b[4]) #this prints a single element in a tuple, in this case "go"


b = bytes()
floatList = [5.4, 3.5, 7.3, 6.8, 4.6]
b = b.join((struct.pack('f', val) for val in floatList))

by=bytearray(b)
print(by)

print(len(by))



