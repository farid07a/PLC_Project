import snap7
from snap7.util import *
from snap7.util import set_string, get_string
import struct
from time import sleep
import random

IP = "192.168.0.1"
RACK = 0
SLOT = 1
plc = snap7.client.Client()
plc.connect(IP, RACK, SLOT)
"===== read Date from Block Date type bool====="
DB_NUMBER = 1  # The date block number to be read.
START_ADDRESS = 0  # Starting Address Reading into Reading Block Date.
SIZE = 3  # Number of bytes to read from Date blocks.
db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)
while True:
    db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)
    print("=====bool=====")
    buffer = bytearray(db)
    print(get_bool(buffer, 0, 0))//0
    print(get_bool(buffer, 0, 1))
    print(get_bool(buffer, 0, 2))

""" 
"===== read Date from Block Date type real====="
START_ADDRESS = 2 # The date block number to be read.
SIZE = 32 # Starting Address Reading into Reading Block Date.
i = 0 # Number of bytes to read from Date blocks.
while True:
 print("===== real=====")
 db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)
 real = struct.iter_unpack("!f", db[:SIZE])
 i += 1
 print("DATA READING:", i, [f for f, in real])
 sleep(1)
"""
# ---write DB---
"""
LS = [10, 10, 9, 12]
real_out = struct.pack("!ffff", LS[0], LS[1], LS[2], LS[3])
plc.db_write(9, 16, real_out)
"""
# ---write DB without end of numbers ( без конца чисел) ---
"""
DB = 9
START_TEG = 16
LS = [0.1, 0.5, 900, 11]
for i in range(0, len(LS)):
 real_out = struct.pack('!f', LS[i])
 plc.db_write(DB, START_TEG, real_out)
 START_TEG += 4
 """
# ---read DB without end of numbers ( без конца чисел) ---
"""DB_NUMBER = 9
START_ADDRESS = 16
SIZE = 16
db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)
real_in = list(struct.iter_unpack("!f", db[:16]))
print(real_in)
"""
# ---Read DB real value---
"""DB_NUMBER = 4
START_ADDRESS = 10
SIZE = 26
i = 0
while True:
 db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)
 real = struct.iter_unpack("!f", db[:16])
 i += 1
 print("DATA READING:", i, [f for f, in real])"""
# ---Read DB Bool value---
"""
print("3 x Bool Vars:", db[8] & 1 == 1, db[8] & 2 == 2, db[8] & 3 == 3, 
db[12] & 4 == 4)
"""
# ---PLC_State---
"""
PLC_State = plc.get_cpu_state()
print(f'{PLC_State}')
"""
# ---str + str ---
"""
LS = [11, 4, 90, 10]
result = ''.join(random.choice('ff') for i in range(0, len(LS)))
result_str = '!' + result
print(result_str)
"""
# ---Create DB in PLC ---
"""
#layout = 
#4 ID NT
#6 NAME STRING[6]
#12.0 testbool1 BOOL
#12.1 testbool2 BOOL
#12.2 testbool3 BOOL
#12.3 testbool4 BOOL
#12.4 testbool5 BOOL
#12.5 testbool6 BOOL
#12.6 testbool7 BOOL
#12.7 testbool8 BOOL
#13 testReal REAL
#17 testDword DWORD
#
IP = "192.168.34.1"
RACK = 0
SLOT = 1
db_number = 2
client = snap7.client.Client()
client.connect(IP, RACK, SLOT)
all_data = client.upload(db_number)
db1 = snap7.util.DB(db_number, all_data, layout,
 17 + 2, 1, id_field='ID',
 layout_offset=0, db_offset=0)
"""
# ---write DB bool without end of numbers ( без конца чисел) ---
"""
IP = "192.168.34.1"
RACK = 0
SLOT = 1
plc = snap7.client.Client()
plc.connect(IP, RACK, SLOT)
DB_NUMBER = 1
START_ADDRESS = 32
SIZE = 2
db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)
while True:
 db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)
 print("=====1=====")
 buffer = bytearray(db)
 print(get_bool(buffer, 0, 0))
 print(get_bool(buffer, 0, 1))
 print(get_bool(buffer, 0, 2))
 print(get_bool(buffer, 0, 3))
 print(get_bool(buffer, 0, 4))
 print(get_bool(buffer, 0, 5))
 print(get_bool(buffer, 0, 6))
 print(get_bool(buffer, 0, 7))
 print("=====2=====")
 print(get_bool(buffer, 1, 0))
 print(get_bool(buffer, 1, 1))
 print(get_bool(buffer, 1, 2))
 print(get_bool(buffer, 1, 3))
 print(get_bool(buffer, 1, 4))
 print(get_bool(buffer, 1, 5))
 print(get_bool(buffer, 1, 6))
 print(get_bool(buffer, 1, 7))
 sleep(1)"""
# ---write value DB real ---
"""DB_NUMBER = 1
START_ADDRESS = 0
SIZE = 2
data = bytearray(4)
x = 222.50112
datat = snap7.util.set_real(data, 0, x)
plc.db_write(DB_NUMBER, START_ADDRESS, datat)"""
# ---write value DB int ---
"""DB_NUMBER = 1
START_ADDRESS = 36
SIZE = 2
data = bytearray(2)
x = 2225
datat = snap7.util.set_int(data, 0, x )
plc.db_write(DB_NUMBER, START_ADDRESS, datat)"""
# ---write value DB real ---
"""DB_NUMBER = 1
START_ADDRESS = 4
SIZE = 16
db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)
data = bytearray(db)
print(snap7.util.get_real(data, 0))"""
# ---write value Q Output bool ---
"""
out_Ren=0
Q_0_0 = 0
Q_0_1 = 0
Q_0_2 = 0
Q_0_3 = 0
Q_0_4 = 0
Q_0_5 = 0
Q_0_6 = 0
Q_0_7 = 0
buffer = bytearray([0b00000000])
set_bool(buffer, 0, 0, Q_0_0)
set_bool(buffer, 0, 1, Q_0_1)
set_bool(buffer, 0, 2, Q_0_2)
set_bool(buffer, 0, 3, Q_0_3)
set_bool(buffer, 0, 4, Q_0_4)
set_bool(buffer, 0, 5, Q_0_5)
set_bool(buffer, 0, 6, Q_0_6)
set_bool(buffer, 0, 7, Q_0_7)
plc.ab_write(out_Ren, buffer)
"""