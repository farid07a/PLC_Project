import sqlite3


class ConnectionSqliteDB:

    __instance = None       # instance of class
    __connection_db = None  # attribute connection

    @classmethod
    def __init_constructor(cls): # return default constructor with class method
        return cls()

    @classmethod
    def get_instance(cls):
        if ConnectionSqliteDB.__instance is None:
            ConnectionSqliteDB.__instance = ConnectionSqliteDB.__init_constructor()  # test if object created

        return ConnectionSqliteDB.__instance

    def connecting(self):
        try:
            ConnectionSqliteDB.__connection_db = sqlite3.connect('D:\database_plc.db')
            print("success connecting")
        # When Error in connection has Occurred
        except sqlite3.Error as e:
            print(e)
    @classmethod
    def get_connection(cls):
        return ConnectionSqliteDB.__connection_db

    @classmethod
    def disconnect(cls):
        ConnectionSqliteDB.__connection_db.close()


obj_cnx = ConnectionSqliteDB.get_instance()
obj_cnx.connecting() #
print(obj_cnx)
print(ConnectionSqliteDB.get_connection())



obj_cnx1 = ConnectionSqliteDB.get_instance()
print(obj_cnx1)
print(ConnectionSqliteDB.get_connection())

obj_cnx.disconnect()

