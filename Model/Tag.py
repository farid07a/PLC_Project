import snap7.util

from snap7.util import get_int, get_real

from Model.ConnectionMysqlDB import ConnectionMysqlDB
import mysql.connector

from Model.ReadData import InputData


class tag:
    ID_Tag = 0
    Name = ""
    Data_Type = ""
    Address_start_byte = 0
    Address_start_bit = 0
    ID_PLC = 0
    connection_mysql = ConnectionMysqlDB()

    # def __init__(self):
    #       self.ID_Tag = 0
    #       self.Name = ""
    #       self.Data_Type = ""
    #       self.Address_start_byte = 0
    #       self.Address_start_bit = 0
    #       self.ID_PLC = 0

    def create_object(self, ID_Tag, Name, Data_Type, Address_start_byte, Address_start_bit, ID_PLC):
        self.ID_Tag = ID_Tag
        self.Name = Name
        self.Data_Type = Data_Type
        self.Address_start_byte = Address_start_byte
        self.Address_start_bit = Address_start_bit
        self.ID_PLC = ID_PLC

    def get_id_tag(self):
        return self.ID_Tag

    def get_name_tag(self):
        return self.Name

    def get_data_type(self):
        return self.Data_Type

    def get_address_start_byte(self):
        return self.Address_start_byte

    def get_address_start_bit(self):
        return self.Address_start_bit

    def get_id_plc(self):
        return self.ID_PLC

    # ------------------------------------------------------#

    def set_id_tag(self, ID_Tag):
        self.ID_Tag = ID_Tag

    def set_id_name(self, Name):
        self.Name = Name

    def set_id_data_type(self, Data_Type):
        self.Data_Type = Data_Type

    def set_id_address_start_byte(self, Address_start_byte):
        self.Address_start_byte = Address_start_byte

    def set_id_address_start_bit(self, Address_start_bit):
        self.Address_start_bit = Address_start_bit

    def set_id_ipl(self, ID_PLC):
        self.ID_PLC = ID_PLC

    def insert_tag_in_database(self):
        # self.set_data_of_tag() used in testing with console
        query = "INSERT INTO tag (Name,Data_Type,Address_start_byte,Address_start_bit,ID_PLC) " \
                "        VALUES (%s  ,%s       ,%s                ,%s               ,%s)"
        cursor = None
        try:
            self.connection_mysql.connecting()
            val = (self.Name, self.Data_Type, self.Address_start_byte, self.Address_start_bit, self.ID_PLC)
            cursor = self.connection_mysql.get_connection().cursor()
            cursor.execute(query, val)
            self.connection_mysql.get_connection().commit()
            print("Success Add Tag")
        except mysql.connector.Error as error:
            print(error)
        finally:
            if self.connection_mysql.get_connection().is_connected():
                self.connection_mysql.get_connection().close()
                cursor.close()

    def set_data_of_tag(self):
        self.Name = input("Input your Tag Name:")
        while True:
            Dtype = int(input("Select Dta_type \n 1 : int \n2 : boolean \n3 : real \n"))

            if Dtype == 1:
                self.Data_Type = "int"
                break

            elif Dtype == 2:
                self.Data_Type = "bool"
                break
            elif Dtype:
                self.Data_Type = "real"
                break
            else:
                print("Select incorrect Choice :")

        self.Address_start_byte = int(input("Input Address Byte :"))
        # list_byte_occupied=self.get_occupied_memory_cases().__getitem__(0)
        # if self.get_address_start_byte in list_byte_occupied:
        #     print("This Adress is reserved:")

        if self.Data_Type == "bool":
            self.Address_start_bit = int(input("Input Address Bit :"))
        else:
            self.Address_start_bit = -1

        self.ID_PLC = int(input("Input PLC Number : "))

    def get_data_tags_in_database(self):
        query = "select * from tag"
        cursor = None
        list_tag = []
        try:
            self.connection_mysql.connecting()
            cursor = self.connection_mysql.get_connection().cursor()
            cursor.execute(query)
            list_tag = cursor.fetchall()
        except mysql.connector.Error as error:
            print(error)
        finally:
            if self.connection_mysql.get_connection().is_connected():
                self.connection_mysql.get_connection().close()
                cursor.close()

        return list_tag

    def list_of_tags(self):  # list of tag object
        data_from_database = self.get_data_tags_in_database()
        list_obj_tags = []
        for row in data_from_database:
            # tag_obj = tag()
            tag_obj = tag()
            tag_obj.create_object(row[0], row[1], row[2], row[3], row[4], row[5])
            list_obj_tags.append(tag_obj)
        return list_obj_tags

    def list_names_of_tags(self):
        list_names=[]
        list_objc_tags = self.list_of_tags()
        for tag_name in list_objc_tags:
            list_names.append(tag_name.get_name_tag())
        return list_names

    def get_size_db(self):
        list_tags = self.list_of_tags()
        size_list_tag = len(list_tags)
        print("Number of Tags :", size_list_tag)

        data_type_last_tag = list_tags[size_list_tag - 1].get_data_type()
        address_last_tag = list_tags[size_list_tag - 1].get_address_start_byte()
        if data_type_last_tag == "int":
            address_last_tag += 2
        elif data_type_last_tag == "real":
            address_last_tag += 4
        elif data_type_last_tag == "bool":
            address_last_tag += 1
        size_data_block = address_last_tag

        return size_data_block

    def get_all_tags_and_time(self):
        cursor = None
        query = "SELECT input_table.ID_Input," \
                " tag.Name, tag.Data_Type, tag.Address_start_bit," \
                "tag_input.Value_Tag," \
                " input_table.Time_Input, plc_controller.ID_PLC " \
                "FROM tag_input, tag, input_table, plc_controller " \
                " WHERE plc_controller.ID_PLC = tag.ID_PLC " \
                " AND tag.ID_Tag = tag_input.ID_Tag " \
                " AND input_table.ID_Input = tag_input.ID_Input" \
                ""
        list_res = []
        try:
            self.connection_mysql.connecting()
            cursor = self.connection_mysql.get_connection().cursor()
            cursor.execute(query)
            list_res = cursor.fetchall()
            for row in list_res:

                id_op = row[0]
                name_tag = row[1]
                data_type = row[2]
                value = 0
                if data_type == "int":
                    value = get_int(row[4], 0)
                elif data_type == "real":
                    value = snap7.util.get_real(row[4], 0)
                elif data_type == "bool":
                    ad_bit = row[3]
                    value = snap7.util.get_bool(row[4], 0, ad_bit)
                # print("ID_op:", id_op, " Name:", name_tag, "data_type:", data_type, " value:", value)


        except mysql.connector.Error as error:
            print(error)
        finally:
            if self.connection_mysql.get_connection().is_connected():
                cursor.close()
                self.connection_mysql.disconnect()
        return list_res


    def get_all_tags_and_time_optimized(self, id_op): # optimize
        cursor = None
        query = "SELECT input_table.ID_Input," \
                " tag.Name, tag.Data_Type, tag.Address_start_bit," \
                "tag_input.Value_Tag," \
                " input_table.Time_Input, plc_controller.ID_PLC " \
                "FROM tag_input, tag, input_table, plc_controller " \
                " WHERE plc_controller.ID_PLC = tag.ID_PLC " \
                " AND tag.ID_Tag = tag_input.ID_Tag " \
                " AND input_table.ID_Input = tag_input.ID_Input " \
                " AND input_table.ID_Input = %s "

        list_res = []

        try:
            self.connection_mysql.connecting()
            cursor = self.connection_mysql.get_connection().cursor()
            cursor.execute(query,(id_op,))
            list_res = cursor.fetchall()
            for row in list_res:

                id_op = row[0]
                name_tag = row[1]
                data_type = row[2]
                value = 0
                if data_type == "int":
                    value = get_int(row[4], 0)
                elif data_type == "real":
                    value = snap7.util.get_real(row[4], 0)
                elif data_type == "bool":
                    ad_bit = row[3]
                    value = snap7.util.get_bool(row[4], 0, ad_bit)
                print("ID_op:", id_op, " Name:", name_tag, "data_type:", data_type, " value:", value)

        except mysql.connector.Error as error:
            print(error)
        finally:
            if self.connection_mysql.get_connection().is_connected():
                cursor.close()
                self.connection_mysql.disconnect()
        return list_res

    def get_occupied_memory_cases(self):
        list_tags = self.list_of_tags()
        memory_cases_occupeid_byte = []
        memory_cases_occupeid_bit = []
        for tag_row in list_tags:
            start_adres_byte = tag_row.get_address_start_byte()

            if tag_row.get_data_type() == "int":
                memory_cases_occupeid_byte.append(start_adres_byte)
                memory_cases_occupeid_byte.append(start_adres_byte + 1)

            elif tag_row.get_data_type() == "real":
                memory_cases_occupeid_byte.append(start_adres_byte)
                for ad in range(start_adres_byte+1, start_adres_byte + 4):
                    print(ad)
                    memory_cases_occupeid_byte.append(ad)
            elif tag_row.get_data_type() == "bool":
                memory_cases_occupeid_byte.append(start_adres_byte)
                start_address_bit = tag_row.get_address_start_bit()
                memory_cases_occupeid_bit.append(str(start_adres_byte) + "_" + str(start_address_bit))
                print("--------------------")
        list_address_byte_and_bit = [memory_cases_occupeid_byte, memory_cases_occupeid_bit]
        return list_address_byte_and_bit

    def get_tag_name_by_address(self,input_address_byte):

        address_tag_db = -1
        name_tag = ""
        list_tags = self.list_of_tags()

        for tag_row in list_tags:
            print("----iteration-------")
            start_adres_byte = tag_row.get_address_start_byte()
            print(start_adres_byte)
            if input_address_byte==start_adres_byte:

                print("Address same input")
                address_tag_db = start_adres_byte
                break

            elif tag_row.get_data_type()== "int" and input_address_byte == start_adres_byte+1:
                print("address not in static address")
                address_tag_db = start_adres_byte
                break
            elif tag_row.get_data_type() == "real" and start_adres_byte < input_address_byte < start_adres_byte + 4:
                address_tag_db = start_adres_byte
                break

        if address_tag_db != -1:
            query="SELECT Name FROM tag WHERE Address_start_byte = %s"
            cursor=None
            try:
                self.connection_mysql.connecting()
                cursor = self.connection_mysql.get_connection().cursor()
                cursor.execute(query, (address_tag_db,))
                tuple_name = cursor.fetchall()
                name_tag = tuple_name[0]
                name_tag = name_tag[0]
            except mysql.connector.Error as error:
                print(error)
            finally:
                if self.connection_mysql.get_connection().is_connected():
                    self.connection_mysql.disconnect()
                    cursor.close()

        return name_tag


# tag_insta = tag()
# # print(tag_insta.get_tag_name_by_address(8))
#
# list_byte_Occupied = tag_insta.get_occupied_memory_cases()
# print(list_byte_Occupied[0])
# print(list_byte_Occupied[1])
#
#
#tag_insta.get_all_tags_between_dates("2022-10-20 12:31:35", "2022-10-24 13:05:22")
#print(tag_insta.get_all_tags_and_time_optimized(1))
# tag_insta.get_all_tags_and_time_optimized(1)
# print(tag_insta.list_names_of_tags())
