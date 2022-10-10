from snap7 import client

class PLC_Controller:

    plc=client.Client()
    def __init__(self, address, rack, slot):

        self.address = address
        self.rack = rack
        self.slot = slot


    def connect(self):

        count = 0

        if  self.plc.get_connected() == False:
            print("Try " + str(count) + " - Connecting to PLC: " +
                    self.address + ", Rack: " + str(self.rack) + ", Slot: " + str(self.slot))
            try:
                plc.connect(self.address, self.rack, self.slot) #('IP-address', rack, slot)
            except Exception as e:
                print(e)

        if  plc.get_connected() == True:
            return plc.get_connected() == True

    def get_word(self,_bytearray, byte_index):
        data = _bytearray[byte_index:byte_index + 2]
        data=data[::-1]
        dword = struct.unpack('H', struct.pack('2B', *data))[0]
        return dword


    def read_data(self):

            torque=plc.read_area(areas['DB'],110,80,24)
            data1=self.get_word(torque,0)

            time.sleep(0.8)
            self.read_data()

    def start_thread(self):
        thread = threading.Thread(target=self.read_data, args=())
        thread.daemon = True
        thread.start()


    def set_word(self,_bytearray, byte_index, word):
        word=int(word)

        _bytes =  struct.pack('H', word)
        _bytes=_bytes[::-1]

        for i, b in enumerate(_bytes):
            time.sleep(1)

            _bytearray[byte_index + i] = b

         res=plc.write_area(areas['DB'],110,24,_bytearray)


    def start_thread2(self):

        thread = threading.Thread(target=self.stoprun, args=())
        thread.daemon = True
        thread.start()

    def stoprun(self):

        Lamp=4
        torque=plc.read_area(areas['DB'],110,80,24)
        val1=self.set_word(torque, 0, 8)
        self.stoprun()
