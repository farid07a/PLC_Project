import snap7
from PLC import plcMachine
# Snap7 client used for connection to a siemens 7 server.

class ConnectionPLC:

    plcMachine = None

    def ConnectingPLC(self,):
        client = snap7.client.Client()
        client.connect("127.0.0.1", 0, 0, 1012)
        client.get_connected()




