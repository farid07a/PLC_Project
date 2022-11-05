from time import sleep
import snap7
from snap7.util import *
from snap7 import client
from Model_Control_.Tag import tag
from Model_Control_.PLC import plcMachine
from Model_Control_.ReadData import InputData
from Model_Control_.SplitDataPackage import SplitDataPackage

IP = "192.168.0.1"
RACK = 0
SLOT = 1


tag_obj = tag()
# plc_obj = plcMachine()
read_data_obj = InputData()
split_data_tag = SplitDataPackage()
plc = client.Client()

try:
    plc.connect(IP, RACK, SLOT)
except:
    print("pass connection physic plc ")


"===== read Date from Block Date type bool====="
DB_NUMBER = 1  # The date block number to be read.
START_ADDRESS = 0  # Starting Address Reading into Reading Block Date.
SIZE = tag_obj.get_size_db_by_id_plc(1) # Number of bytes to read from Date blocks.
print("Size Of data Block :",SIZE)

# db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE) # REPLACE by test db byteArray


db = bytearray(20)

set_int(db,0,40)
set_real(db,2,40.5)
set_bool(db,6,0,0)
set_bool(db,6,1,0)
set_real(db,7,40.40)


print("db array :", db)

read_data_obj.Data_Input = db  # set dataBloc to DataInput to save with operation
read_data_obj.insert_input_data() # save The operation read of data with primary key
list_tags = tag_obj.list_of_tags_by_id_plc(1)      # get list of tags to get id

for tag_i in list_tags:

    id_tag = tag_i.get_id_tag()
    data_type = tag_i.get_data_type()
    addres_byte = tag_i.get_address_start_byte()

    print("ID_tag:",id_tag ,"data_type:",data_type,"addres_byte:",addres_byte,"End_adres_byte",addres_byte+2)
    part_of_tag=bytearray(4)

    if data_type == "int":
        part_of_tag = db[addres_byte:addres_byte + 2]
        print("part of package from db :", part_of_tag)
        print(get_int(db, addres_byte))

    elif data_type == "real":
        part_of_tag = db[addres_byte:addres_byte + 4]
        print(get_int(db, addres_byte))

    elif data_type == "bool":
        addres_bit = tag_i.get_address_start_bit()
        part_of_tag = db[addres_byte:addres_byte + 1]
        print(snap7.util.get_bool(db, addres_byte, addres_bit))

    id_read= read_data_obj.get_last_operation_read() # return last id of Operation Read
    print("Last ID of Operationread :",id_read)
    split_data_tag.create(id_tag, id_read, part_of_tag) #
    split_data_tag.insert_split_data_package_database() # insert data in database




