from time import sleep
import snap7
from snap7.util import *
from snap7 import client

from Model.PLC import plcMachine
from Model.ReadData import InputData

IP = "192.168.0.1"
RACK = 0
SLOT = 1

from Model.Tag import tag

tag = tag()
plc_obj = plcMachine()

read_data_obj= InputData()

plc = client.Client()

plc.connect(IP, RACK, SLOT)

"===== read Date from Block Date type bool====="
DB_NUMBER = 1  # The date block number to be read.
START_ADDRESS = 0  # Starting Address Reading into Reading Block Date.
SIZE = 54  # Number of bytes to read from Date blocks.



while True:

    if plc.get_connected():

        db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)
        read_data_obj.Data_Input=db

        read_data_obj.insert_input_data() # save The operation read of data with primary key
        list_tags=tag.list_of_tags()      # get list of tags to get id and

        for tag_i in list_tags:

            id_tag = tag_i.get_id_tag()
            data_type = tag_i.get_data_type()
            addres_byte = tag_i.get_address_start_byte()
            addres_bit = tag_i.get_address_start_bit()
            part_of_tag=bytearray()
            if data_type=="int":
                part_of_tag=db[addres_byte:addres_byte + 2]
                print(int.from_bytes(part_of_tag,"big") )
                #get_int(db,addres_byte) Python : dtype = 4 byte
            elif data_type=="real":
                part_of_tag = db[addres_byte:addres_byte + 4]
                print(float.from_bytes(part_of_tag, "big"))
                # get_real(db,addres_byte) Python : dtype = 8 byte
            else:
                part_of_tag=db[addres_byte:addres_byte + 1]
                print()



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

""""
 get_exec_time
 get_last_error
 get_order_code
 get_cpu_state()

 buffer = bytearray([0b00000000])
plc.db_write(1, 0, buffer)


plc_info = plc.get_cpu_info()
print(f"adı: {plc_info.ModuleTypeName}")
buffer = bytearray(db)
print(plc.get_cpu_info())
print(plc.get_plc_datetime())
sleep(2)

    db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)
    print("=====bool=====")
    buffer = bytearray(db)
    print(get_bool(buffer, 0, 0))
    print(get_bool(buffer, 0, 1))
    print(get_bool(buffer, 0, 2))

===== read Date from Block Date type real====="
START_ADDRESS = 2  # The date block number to be read.
SIZE = 32  # Starting Address Reading into Reading Block Date.
i = 0  # Number of bytes to read from Date blocks.
while True:
    print("===== real=====")
    db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)
    real = struct.iter_unpack("!f", db[:SIZE])
    i += 1
    print("DATA READING:", i, [f for f, in real])
    sleep(1)"""
