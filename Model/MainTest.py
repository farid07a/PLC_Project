from time import sleep
import snap7
from snap7.util import *
from snap7 import client
from Model.Tag import tag
from Model.PLC import plcMachine
from Model.ReadData import InputData
from Model.SplitDataPackage import SplitDataPackage

IP = "192.168.0.1"
RACK = 0
SLOT = 1



tag = tag()
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
SIZE = tag.get_size_db() # Number of bytes to read from Date blocks.
print("Size Of data Block :",SIZE)

# db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE) # REPLACE by test db byteArray
rList = [1, 0, 3, 0, 5,0]



db=bytearray(rList)

db=bytearray(20)

snap7.util.set_int(db,0,154)
snap7.util.set_real(db,2,40.5)
snap7.util.set_bool(db,6,0,0)
snap7.util.set_bool(db,6,1,1)
snap7.util.set_real(db,7,0.78)

print("db array :", db)

read_data_obj.Data_Input = db  # set dataBloc to DataInput to save with operation
read_data_obj.insert_input_data() # save The operation read of data with primary key
list_tags = tag.list_of_tags()      # get list of tags to get id and

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
        part_of_tag
    elif data_type == "bool":
        addres_bit = tag_i.get_address_start_bit()
        part_of_tag = db[addres_byte:addres_byte + 1]
        print(snap7.util.get_bool(db, addres_byte, addres_bit))


    id_read= read_data_obj.get_last_operation_read() # return last id of Operation Read
    print("Last ID of Operationread :",id_read)

    split_data_tag.create(id_tag, id_read, part_of_tag) #

    split_data_tag.insert_split_data_package_database() # insert data in database





var =True
while var:

    if plc.get_connected():





        print(db)

        print(get_bool(db, 0, 0))
        print(get_bool(db, 0, 1))
        print(get_bool(db, 0, 2))
        print(get_bool(db, 0, 3))
        print(get_bool(db, 0, 4))
        print(get_bool(db, 0, 5))
        print(get_bool(db, 0, 6))
        print(get_bool(db, 0, 7))
        print(get_bool(db, 1, 0))

        print(get_bool(db, 1, 1))
        print(get_int(db, 46))
        print("--------------")
        # insert tags(in DB)

        sleep(1)
    else:
        print("PLC no connected")
        break


