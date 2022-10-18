from Model.ConnectionMysqlDB import ConnectionMysqlDB


class tag:

    ID_Tag =0
    Name = ""
    Data_Type = ""
    Address_start_byte = 0
    Address_start_bit =0
    ID_PLC=0
    connection_mysql = ConnectionMysqlDB()

    # def __init__(self):
    #      self.ID_Tag = 0
    #      self.Name = ""
    #      self.Data_Type = ""
    #      self.Address_start_byte = 0
    #      self.Address_start_bit = 0
    #      self.ID_PLC = 0

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
        self.ID_Tag=ID_Tag

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

    # def test_connecttion(self):
    #     print("")
    #     try:
    #         if not self.var_connection.is_connected():
    #             print("Var myf Connection : ", self.var_connection.is_connected())
    #             self.var_connection=mysql.connector.connect(host='localhost', user='root', passwd='', database='myf')
    #             print("Success Connecting dataBase")
    #         else:
    #             print("Deja connecting")
    #
    #     except BaseException as e:
    #         print(e)
    #         sleep(1)
    #         self.test_connecttion()
    def insert_tag_in_database(self):
        self.set_data_of_tag()
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
        except BaseException as e:
            print(e)
        finally:
            if self.connection_mysql.get_connection().is_connected():
                self.connection_mysql.get_connection().close()
                cursor.close()

    def set_data_of_tag(self):
        self.Name = input("Input your Tag Name:")
        while True:
            Dtype = int(input("Select Dta_type \n1 : int \n2 : boolean\n3 : real "))
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
            cursor=self.connection_mysql.get_connection().cursor()
            cursor.execute(query)
            list_tag=cursor.fetchall()
        except:
            print("Error connection")
        finally:
            if self.connection_mysql.get_connection().is_connected():
                self.connection_mysql.get_connection().close()
                cursor.close()

        return list_tag

    def list_of_tags(self):
        data_from_database = self.get_data_tags_in_database()
        list_obj_tags=[]
        for row in data_from_database:
            tag_obj = tag()
            tag_obj.create_object(row[0],row[1],row[2],row[3],row[4],row[5])
            list_obj_tags.append(tag_obj)
        return list_obj_tags

    def reserverd_adress_db(self):
        print("")

    def menu_inert_tag(self):
        c='a'
        #while c!= 'q':










