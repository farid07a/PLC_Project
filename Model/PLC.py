from snap7 import client
class plcMachine (client):

    IdPlc = 0
    IP = ""
    RACK = 0
    SLOT = 1
    Status = True
    ModelPlc = ""

    def __init__(self,IdPlc, IP, RACK, SLOT,Status,ModelPlc ):
        self.IdPlc = IdPlc
        self.IP = IP
        self.RACK = RACK
        self.SLOT = SLOT
        self.Status = Status
        self.ModelPlc = ModelPlc

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


