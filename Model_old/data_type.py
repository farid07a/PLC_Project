
class DataType:

    VARCHAR = "VARCHAR(50)"
    BINARY = "BINARY"
    BIT = "BIT"
    BOOL = "BOOL"
    INT = "INT"
    FLOAT = "FLOAT"
    def __init__(self):
        VARCHAR = "VARCHAR(50)"
        BINARY = "BINARY"
        BIT = "BIT"
        BOOL = "BOOL"
        INT = "INT"
        FLOAT = "FLOAT"

    def get_int(self):
        return self.INT

    def get_binary(self):
        return self.BINARY

    def get_bit(self):
        return self.BIT

    def get_bool(self):
        return self.BOOL

    def get_varchar(self):
        return self.VARCHAR

    def get_float(self):
        return self.FLOAT
