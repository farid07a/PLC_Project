from snap7 import client
class plcMachine (client):

    IdPlc = 0
    IP = ""
    RACK = 0
    SLOT = 1
    Status = True
    ModelPlc = ""
    clientPlc = client.Client()
    ConnectionObj=False

    def __init__(self,IdPlc, IP, RACK, SLOT ):
        self.IdPlc = IdPlc
        self.IP = IP
        self.RACK = RACK
        self.SLOT = SLOT


    def connecting(self):

        try:
            if not self.clientPlc.get_connected():
                self.clientPlc.connect(self.IP,self.RACK,self.SLOT)
                self.ConnectionObj=True
        except Exception as e:
            print(e)



    def connectingRecursion(self):

        try:
            if self.ConnectionObj==False:
                self.clientPlc.connect(self.IP,self.RACK,self.SLOT)
                self.ConnectionObj=True
        except Exception as e:
            print("Occured Exception")



    def getClientPLC(self):
        return self.clientPlc

    def setClientPLC(self, clientPlc):



    def setIdPlc(self,IdPlc):
        self.IdPlc = IdPlc

    def getIdPlc(self):
        return self.IdPlc

    def setIP(self,IP):
        self.IP = IP

    def getIP(self):
        return self.IP

    def setSolt(self,SLOT):
        self.SLOT=SLOT

    def getSlot(self):
        return self.SLOT

    def setRack(self,RACK):
        self.RACK=RACK

    def getRACK(self):
        return self.RACK

    def AddNewPLC(self):
        Query = "INSERT INTO PLC () values ("


