import pyodbc


try:
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SOFT\SQLEXPRESS;'
                        'Database=database_plc;'
                      'Trusted_Connection=yes;')
    print("Success Connecting")
except :
    print("Error connecting")