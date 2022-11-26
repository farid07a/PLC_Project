class ConnectionFactory(object):
    def __init__(self, acceptable_types):
        self.__db = None

    """This interface defines an object that is able to make database connections.
    This allows database connections to be defined inside application contexts, and
    fed to DAO and DatabaseTemplates."""

    def connect(self):
        raise NotImplementedError()

    def getConnection(self):
        if self.__db is None:
            self.__db = self.connect()
        return self.__db

    def close(self):
        "Need to offer API call to close the connection to the database."
        if self.__db is not None:
            self.__db.close()
            self.__db = None

    def commit(self):
        if self.in_transaction():
            self.getConnection().commit()

    def rollback(self):
        if self.in_transaction():
            self.getConnection().rollback()

    def in_transaction(self):
        raise NotImplementedError()

    def count_type(self):
        raise NotImplementedError()

    def convert_sql_binding(self, sql_query):
        """This is to help Java users migrate to Python. Java notation defines binding variables
        points with '?', while Python uses '%s', and this method will convert from one format
        to the other."""
        return re.sub(pattern="\?", repl="%s", string=sql_query)