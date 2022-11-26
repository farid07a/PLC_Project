from time import sleep

import sqlite3


class ConnectionSqliteDB:
    __connection_db = None

    @classmethod
    def connecting(cls):
        try:
            ConnectionSqliteDB.__connection_db = sqlite3.connect('L:\database_plc.db')
            # self.connection_db = sqlite3.connect('\\Model_old\\database_plc.db')
            print("success connecting")
        # When Error in connection has Occurred
        except sqlite3.Error as e:
            print(e)

    @classmethod
    def get_connection(cls):
        return ConnectionSqliteDB.__connection_db

    @classmethod
    def set_connection(cls, connection_db):
        ConnectionSqliteDB.__connection_db = connection_db

    @classmethod
    def disconnect(cls):
        ConnectionSqliteDB.__connection_db.close()


ConnectionSqliteDB.connecting()
print(ConnectionSqliteDB.get_connection())


