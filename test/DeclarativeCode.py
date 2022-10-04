from builtins import input

import snap7
IP="172.16.5.100"
RACK=0
SLOT=1

PlcClient = snap7.client.Client()
PlcClient.connect(IP, RACK, SLOT,102)
StatusConnection = PlcClient.get_connected()

if StatusConnection:
    print("Succes Connect \n")
else:
    print("Failed To connecting")
PlcInfo = PlcClient.get_cpu_info() # obj:`S7CpuInfo`: data structure with the information.
print(PlcInfo, "\n")
PlcStatus = PlcClient.get_cpu_state();
print(PlcStatus)


#print("Please Input Number Of Block:")
DB_NUMBER = int(input("Enter Your DB Number :"))
STAR_ADDRESS = int(input("Enter FIRST Address"))
SIZE_Byte = int(input("Enter size Byte you want to read and Save it In array Of bytes"))

PlcClient.ab_read(DB_NUMBER,STAR_ADDRESS,SIZE_Byte)
# Return Array Of BYte



