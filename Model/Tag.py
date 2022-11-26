import snap7.util
from snap7.util import get_int
import sqlite3
from Model.ConnectionSqliteDB import ConnectionSqliteDB


class Tag:

    def __init__(self, ID_Tag, Name, Data_Type, Address_start_byte, Address_start_bit, ID_PLC):
        self.__ID_Tag = ID_Tag
        self.__Name = Name
        self.__Data_Type = Data_Type
        self.__Address_start_byte = Address_start_byte
        self.__Address_start_bit = Address_start_bit
        self.__ID_PLC = ID_PLC



    def create_object(self, ID_Tag, Name, Data_Type, Address_start_byte, Address_start_bit, ID_PLC):
        self.__ID_Tag = ID_Tag
        self.__Name = Name
        self.__Data_Type = Data_Type
        self.__Address_start_byte = Address_start_byte
        self.__Address_start_bit = Address_start_bit
        self.__ID_PLC = ID_PLC

    @classmethod
    def init_default_tag(cls):
        return cls()


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

    # insert tag fields in database
    def insert_tag_in_database(self):
        query = "INSERT INTO tag (Name,Data_Type,Address_start_byte,Address_start_bit,ID_PLC) " \
                "        VALUES (?  ,?       ,?                ,?               ,?)"
        try:
            ConnectionSqliteDB.get_instance().connecting()
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

    # for testing to insert tag
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
        # print("This Address is reserved:")

        if self.Data_Type == "bool":
            self.Address_start_bit = int(input("Input Address Bit :"))
        else:
            self.Address_start_bit = -1

        self.ID_PLC = int(input("Input PLC Number : "))

    # use for all PLCs
    # function to get list tags from database sqlite
    # maintain close() func
    # return list of tuple (id_tag,name,datatype,adres_Byt,AdresBit,Idplc)
    @staticmethod
    def __get_list_tags_in_database():
        query = "select * from tag"
        list_tag = []
        try:
            ConnectionSqliteDB.get_instance().connecting()
            cursor = ConnectionSqliteDB.get_instance().get_connection().cursor()
            cursor.execute(query)
            list_tag = cursor.fetchall()
            cursor.close()
        except sqlite3.Error as error:
            print(error)
        finally:
            if ConnectionSqliteDB.get_connection():
                ConnectionSqliteDB.disconnect()

        return list_tag

    # get list tags from database with id_plc
    # return list of tuple (id_tag,name,datatype,adres_Byt,AdresBit,Idplc)
    # maintain cursor.close()

    # TO DO change __get_list_tags_in_database_by_id_plc by __get_list_tags_in_database (overloading)
    @staticmethod
    def __get_list_tags_in_database(id_plc):
        query = "select * from  tag WHERE tag.ID_PLC = ? "
        list_tag = []
        try:
            ConnectionSqliteDB.get_instance().connecting()
            cursor = ConnectionSqliteDB.get_instance().get_connection().cursor()
            cursor.execute(query, (id_plc,))
            list_tag = cursor.fetchall()
            for tag_row in list_tag:
                print(tag_row)
            cursor.close()
        except sqlite3.Error as error:
            print(error)
        finally:
            if ConnectionSqliteDB.get_connection():
                ConnectionSqliteDB.disconnect()

        return list_tag

    # get list tag obj by ip_address
    # use static get_data_tags_in_database(id_plc)

    def __get_list_objects_of_tag_by_id_plc(self, id_plc):  # list of tag object

        data_from_database = Tag.__get_list_tags_in_database(id_plc)
        list_obj_tags = []
        for row in data_from_database:
            # tag_obj = tag()
            tag_obj = self.__init__(row[0], row[1], row[2], row[3], row[4], row[5])
            list_obj_tags.append(tag_obj)
            print(list_obj_tags[0])
        return list_obj_tags

    # get list of tag obj(args,...)
    # use static method __get_list_tags_in_database()
    def __get_list_objects_of_tag(self):
        data_from_database = Tag.__get_list_tags_in_database()
        list_obj_tags = []
        for row in data_from_database:
            tag_obj = self.__init__(row[0], row[1], row[2], row[3], row[4], row[5])
            list_obj_tags.append(tag_obj)
        return list_obj_tags

    # invalid
    # get list names of tags in database
    # return list_names = ['tag1', 'tag2',...,'tag3']
    def list_names_of_tags(self):
        list_names = []
        list_objc_tags = self.__get_list_objects_of_tag()
        for tag_name in list_objc_tags:
            list_names.append(tag_name.get_name_tag())
        return list_names

    # get list names of tags in database with id_plc
    # return list_names = ['tag1', 'tag2',...,'tag3']

    def list_names_of_tags_by_id_plc(self, id_plc):
        list_names = []
        list_objc_tags = self.__get_list_objects_of_tag_by_id_plc(id_plc)
        for tag_name in list_objc_tags:
            list_names.append(tag_name.get_name_tag())
        return list_names

    # get size of db automatically when read and write
    def get_size_db(self):
        list_tags = self.__get_list_objects_of_tag()
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

    # get size db automatically of id_plc
    # return size=>int
    def get_size_db_by_id_plc(self, id_plc):
        list_tags = self.__get_list_objects_of_tag_by_id_plc(id_plc)
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

    # get list of join data
    # return list of tuple(ID_Input,Name,Data_Type,Address_start_bit,Value_Tag,Time_Input,ID_PLC)
    def get_all_tags_and_time(self):
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
            self.connection_sqlite.connecting()
            cursor = self.connection_sqlite.get_connection().cursor()
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
            cursor.close()
        except sqlite3.Error as error:
            print(error)
        finally:
            if self.connection_sqlite.get_connection():
                self.connection_sqlite.disconnect()
        return list_res

    # valid function
    # get join data by join query instead old query  with id_op
    # return list of tuple = (ID_Input,Name,Data_Type,Address_start_bit,Value_Tag,Time_Input,ID_PLC)
    # arg : id_id_op  id_operation for tags related
    def get_all_tags_and_time_optimized(self, id_op):  # optimize
        query = " SELECT input_table.ID_Input," \
                " tag.Name, tag.Data_Type, tag.Address_start_bit," \
                " tag_input.Value_Tag," \
                " input_table.Time_Input, plc_controller.ID_PLC " \
                " FROM tag_input, tag, input_table, plc_controller " \
                " WHERE plc_controller.ID_PLC = tag.ID_PLC " \
                " AND tag.ID_Tag = tag_input.ID_Tag " \
                " AND input_table.ID_Input = tag_input.ID_Input " \
                " AND input_table.ID_Input = ? "
        # change old join by join query
        query1 = "SELECT * FROM plc_controller p JOIN tag t ON p.ID_PLC= t.ID_PLC " \
                 "JOIN tag_input ti ON ti.ID_Tag = t.ID_Tag " \
                 "JOIN input_table i ON i.ID_Input=ti.ID_Input WHERE i.ID_Input = ? "
        list_res = []
        try:
            self.connection_sqlite.connecting()
            cursor = self.connection_sqlite.get_connection().cursor()
            cursor.execute(query, (id_op,))
            list_res = cursor.fetchall()

            print(list_res)

            for row in list_res:
                id_op = row[0]
                print("id_op", id_op)
                name_tag = row[1]
                print("name:", name_tag)
                data_type = row[2]
                print("datatype", data_type)

                print(row[4])

                # get_int(row[4], 0)
                value = 0
                if data_type == "int":
                    # value = get_int(row[4], 0)
                    # print(row[4])
                    value = int.from_bytes(row[4], 'big')
                elif data_type == "real":
                    # value = snap7.util.get_real(row[4], 0)
                    # [x] = struct.unpack('f', row[4])
                    # value = x
                    value = snap7.util.get_real(row[4], 0)
                elif data_type == "bool":
                    ad_bit = row[3]
                    value = snap7.util.get_bool(row[4], 0, ad_bit)
                print("value : ", row[4], ":  ", value)
                print("time", row[5])
                print("id_plc", row[6])
                print("-----------------------------------------------")
                # print("ID_op:", id_op, " Name:", name_tag, "data_type:", data_type, " value:", value)
            cursor.close()
        except sqlite3.Error as error:
            print(error)
        finally:
            if self.connection_sqlite.get_connection():
                self.connection_sqlite.disconnect()
        return list_res

    # invalid function
    # get join data by join query instead old query  with id_op
    #  result by dictionary = [ dict[ID_Input:"value"],dict[Name:"value"],dict[Data_Type:"value"] ]
    # return list of tuple = (id_op, name_tag, data_type, ad_bit, value, row["Time_Input"], row["ID_PLC"])
    # arg : id_id_op  id_operation to get related tags
    def get_all_tags_and_time_optimized_query_update(self, id_op):  # optimize by return dictionary

        query1 = "SELECT * FROM plc_controller p " \
                 "JOIN tag t ON p.ID_PLC= t.ID_PLC " \
                 "JOIN tag_input ti ON ti.ID_Tag = t.ID_Tag " \
                 "JOIN input_table i ON i.ID_Input=ti.ID_Input " \
                 "WHERE i.ID_Input= ? "

        list_res = []
        try:
            self.connection_sqlite.connecting()
            cursor = self.connection_sqlite.get_connection().cursor(dictionary=True)
            cursor.execute(query1, (id_op,))
            result = cursor.fetchall()

            for row in result:
                id_op = row["ID_Input"]
                name_tag = row["Name"]
                data_type = row["Data_Type"]
                value = 0
                ad_bit = -1
                if data_type == "int":
                    value = get_int(row["Value_Tag"], 0)
                elif data_type == "real":
                    value = snap7.util.get_real(row["Value_Tag"], 0)
                elif data_type == "bool":
                    ad_bit = row["Address_start_bit"]
                    value = snap7.util.get_bool(row["Value_Tag"], 0, ad_bit)

                tup = (id_op, name_tag, data_type, ad_bit, value, row["Time_Input"], row["ID_PLC"])
                print("ID_op:", id_op, " Name:", name_tag, "data_type:", data_type, " value:", value, " time:",
                      row["Time_Input"], " ID_PLC:", row["ID_PLC"])
                print("tuple data:", tup)
                list_res.append(tup)

                cursor.close()
        except sqlite3.Error as error:
            print(error)
        finally:
            if self.connection_sqlite.get_connection():
                self.connection_sqlite.disconnect()
        return list_res

    # Invalid function because have many plc
    # get all  reserved address in db
    # return list =[ memory_cases_occupeid_byte,memory_cases_occupeid_bit]
    # arg id_plc

    def get_occupied_memory_cases(self):
        list_tags = self.__get_list_objects_of_tag()
        memory_cases_occupeid_byte = []
        memory_cases_occupeid_bit = []
        for tag_row in list_tags:
            start_adres_byte = tag_row.get_address_start_byte()

            if tag_row.get_data_type() == "int":
                memory_cases_occupeid_byte.append(start_adres_byte)
                memory_cases_occupeid_byte.append(start_adres_byte + 1)

            elif tag_row.get_data_type() == "real":
                memory_cases_occupeid_byte.append(start_adres_byte)
                for ad in range(start_adres_byte + 1, start_adres_byte + 4):
                    print(ad)
                    memory_cases_occupeid_byte.append(ad)
            elif tag_row.get_data_type() == "bool":
                memory_cases_occupeid_byte.append(start_adres_byte)
                start_address_bit = tag_row.get_address_start_bit()
                memory_cases_occupeid_bit.append(str(start_adres_byte) + "_" + str(start_address_bit))
                print("--------------------")
        list_address_byte_and_bit = [memory_cases_occupeid_byte, memory_cases_occupeid_bit]
        return list_address_byte_and_bit

    # get all  reserved address in plc
    # return list =[ memory_cases_occupeid_byte,memory_cases_occupeid_bit]
    # arg id_plc
    def get_occupied_memory_cases_by_id_plc(self, id_plc):
        list_tags = self.__get_list_objects_of_tag_by_id_plc(id_plc)
        memory_cases_occupeid_byte = []
        memory_cases_occupeid_bit = []
        for tag_row in list_tags:
            start_adres_byte = tag_row.get_address_start_byte()
            if tag_row.get_data_type() == "int":
                memory_cases_occupeid_byte.append(start_adres_byte)
                memory_cases_occupeid_byte.append(start_adres_byte + 1)

            elif tag_row.get_data_type() == "real":
                memory_cases_occupeid_byte.append(start_adres_byte)
                for ad in range(start_adres_byte + 1, start_adres_byte + 4):
                    print(ad)
                    memory_cases_occupeid_byte.append(ad)
            elif tag_row.get_data_type() == "bool":
                memory_cases_occupeid_byte.append(start_adres_byte)
                start_address_bit = tag_row.get_address_start_bit()
                memory_cases_occupeid_bit.append(str(start_adres_byte) + "_" + str(start_address_bit))
                print("--------------------")
        list_address_byte_and_bit = [memory_cases_occupeid_byte, memory_cases_occupeid_bit]
        return list_address_byte_and_bit

    # get name tag for address byte reserved in plc
    # arg: id_plc , address byte reserved
    def get_tag_name_by_address(self, id_plc, input_address_byte):
        address_tag_db = -1
        name_tag = ""
        list_tags = self.__get_list_objects_of_tag_by_id_plc(id_plc)

        for tag_row in list_tags:
            print("----iteration-------")
            start_adres_byte = tag_row.get_address_start_byte()
            print(start_adres_byte)
            if input_address_byte == start_adres_byte:

                print("Address same input")
                address_tag_db = start_adres_byte
                break

            elif tag_row.get_data_type() == "int" and input_address_byte == start_adres_byte + 1:
                print("address not in static address")
                address_tag_db = start_adres_byte
                break
            elif tag_row.get_data_type() == "real" and start_adres_byte < input_address_byte < start_adres_byte + 4:
                address_tag_db = start_adres_byte
                break

        if address_tag_db != -1:
            query = "SELECT Name FROM tag WHERE Address_start_byte = ? AND ID_PLC = ?"
            try:
                self.connection_sqlite.connecting()
                cursor = self.connection_sqlite.get_connection().cursor()
                cursor.execute(query, (address_tag_db, id_plc))
                tuple_name = cursor.fetchall()
                name_tag = tuple_name[0]
                name_tag = name_tag[0]
                cursor.close()
            except sqlite3.Error as error:
                print(error)
            finally:
                if self.connection_sqlite.get_connection():
                    self.connection_sqlite.disconnect()

        return name_tag

    def get_id_tag_from_database(self, id_plc, name):
        query = "SELECT ID_Tag FROM tag WHERE ID_PLC = ?  AND Name = ? "
        self.connection_sqlite.connecting()
        id_tag = 0
        try:
            cursor = self.connection_sqlite.get_connection().cursor()
            cursor.execute(query, (id_plc,name))
            result = cursor.fetchone()
            print("result:",result)
            id_tag = result[0]
            print("id_tag:",id_tag)
            cursor.close()
        except sqlite3.Error as error:
            print(error)
        finally:
            if self.connection_sqlite.get_connection():
                self.connection_sqlite.disconnect()
        return id_tag


    def delete_tag(self, id_tag):
        query = "DELETE FROM tag WHERE ID_Tag=? "
        row_count=0
        try:
            self.connection_sqlite.connecting()
            cursor = self.connection_sqlite.get_connection().cursor()
            cursor.execute(query, (id_tag,))
            print("Row count :", cursor.rowcount)
            row_count = cursor.rowcount
            self.connection_sqlite.get_connection().commit()
            cursor.close()

        except sqlite3.Error as error:
            print(error)
        finally:
            if self.connection_sqlite.get_connection():
                self.connection_sqlite.disconnect()
        return row_count

    def get_id_plc_from_database(self, id_tag):
        query = "SELECT  ID_PLC FROM tag WHERE ID_Tag=?"
        id_plc_val = 0
        try:
            self.connection_sqlite.connecting()
            cursor = self.connection_sqlite.get_connection().cursor()
            cursor.execute(query, (id_tag,))
            id_plc = cursor.fetchone()
            id_plc_val = id_plc[0]
            cursor.close()
        except sqlite3.Error as error:
            print(error)
        finally:
            if self.connection_sqlite.get_connection():
                self.connection_sqlite.get_connection().close()
        return id_plc_val

    def get_max_id_tag(self, connection):
        query = "SELECT MAX(ID_Tag) FROM  tag"
        last_id = 0
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            last_id = result[0]
            print("Max id_tag_in_plc"," :",last_id)
        except sqlite3.Error as error:
            print(error)
        return last_id
    # this use when delete all tags and initialise id_tag to zero
    def reset_increment_id_tag(self,max_id,connection):
        query = "UPDATE SQLITE_SEQUENCE SET SEQ=? WHERE NAME='tag';"
        last_id = 0
        try:
            cursor = connection.cursor()
            cursor.execute(query,(max_id,))

        except sqlite3.Error as error:
            print(error)

    def update_tag_info(self,id_tag):
        print(id_tag)
        query= " UPDATE tag SET Name=? , Data_Type=? ,Address_start_byte=?," \
               " Address_start_bit=?, ID_PLC=?" \
               " WHERE ID_Tag = ?"
        row_count = 0
        try:
            self.connection_sqlite.connecting()
            cursor = self.connection_sqlite.get_connection().cursor()
            cursor.execute(query, (self.Name,self.Data_Type,self.Address_start_byte,self.Address_start_bit,self.ID_PLC,id_tag))
            row_count = cursor.rowcount
            self.connection_sqlite.get_connection().commit()

            cursor.close()
        except sqlite3.Error as error:
            print(error)
        finally:
            if self.connection_sqlite.get_connection():
                self.connection_sqlite.disconnect()
        return row_count


# pass testing
# insert_tag_in_database
# tag_insta.get_data_tags_in_database_by_id_plc(id_plc)
# __get_list_objects_of_tag_by_id_plc(id_plc)
# get_tag_name_by_address(id_plc,address_byte)
# get_occupied_memory_cases_by_id_plc(id_plc)
# tag_insta = tag()
# idtag=tag_insta.get_id_tag_from_database(1, "tag_upd_3_3")

# print(idtag)
#
# tag_insta.update_tag_info(tag_insta.get_id_tag())
# print(tag_insta.__get_list_objects_of_tag_by_id_plc(1))
# print("---------------")
# tag_insta.get_data_tags_in_database_by_id_plc(1)
# print("---------------")
#
# print(tag_insta.get_tag_name_by_address(1,2))
# lisResevedByte=tag_insta.get_occupied_memory_cases_by_id_plc(1)
#
# print(lisResevedByte[0])
# print(lisResevedByte[1])

# listtags=tag_insta.get_all_tags_and_time_optimized_query_update(1)
#
# print("------------------")
#
# print(listtags)

# print(tag_insta.__get_list_objects_of_tag())

#
# list_byte_Occupied = tag_insta.get_occupied_memory_cases()
# print(list_byte_Occupied[0])
# print(list_byte_Occupied[1])
#
#
# tag_insta.get_all_tags_between_dates("2022-10-20 12:31:35", "2022-10-24 13:05:22")
# print(tag_insta.get_all_tags_and_time_optimized(1))
# list_tags = tag_insta.get_all_tags_and_time_optimized(1)
# print(len(tag_insta.get_all_tags_and_time_optimized(1)))

# print(tag_insta.list_names_of_tags())
