import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=L:\databasePLC.accdb;'
    conn = pyodbc.connect(con_string)
    print("Connected To Database")

# L:\databasePLC.accdb

except pyodbc.Error as e:
    print("Error in Connection", e)