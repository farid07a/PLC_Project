

import pyodbc
[x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')]


# cnxn = pyodbc.connect("DRIVER={Microsoft Access Driver (*.mdb),(*.accdb)};DBQ=D:\Base de donnéesplc.accdb;")
#
# print(cnxn)
