import snap7

IP="172.16.5.100"
RACK=0
SLOT=1
def connectToPlc_GetInstancePLC():
    """Creates a new `Client` instance.

            Args:
                lib_location: Full pat to the snap7.dll file. Optional.
                 client = snap7.client.Client()  # If the `snap7.dll` file is in the path location
                client = snap7.client.Client(lib_location="/path/to/snap7.dll")  # If the `snap7.dll` file is in another location
                 client
                <snap7.client.Client object at 0x0000028B257128E0>
            """

    PlcDevice = snap7.client.Client()  #Creates a new `Client` instance.
    PlcDevice.connect(IP, RACK, SLOT) #  Connects a Client Object to a PLC. default port  102
    """
    Args:
            address: IP address of the PLC.
            rack: rack number where the PLC is located.
            slot: slot number where the CPU is located.
            tcpport: port of the PLC.
    """
    ErrorConnection = PlcDevice.get_connected() #
    print(ErrorConnection) # Display True Or False When Connection Ressource Not Connected
    if ErrorConnection:
        return PlcDevice
    else:
        return None

def DetaillsOfPlc():
    plc_device = connectToPlc_GetInstancePLC()
    plc_Infor=plc_device.get_cpu_info()

    print(plc_Infor)

