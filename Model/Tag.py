from time import sleep

import mysql.connector
class tag:

    id =0
    NameTag = ""
    Value = bytearray()
    start = 0
    size =0
    var_connection=mysql.connector.connect()
    def __init__(self,id,NameTag,Value,start,size):
        self.id=id
        self.NameTag=NameTag
        self.Value=Value
        self.start=start
        self.size= size


    def test_connecttion(self):
        print("")
        try:
            if not self.var_connection.is_connected():
                print("Var myf Connection : ", self.var_connection.is_connected())
                self.var_connection=mysql.connector.connect(host='localhost', user='root', passwd='', database='myf')
                print("Success Connecting dataBase")
            else:
                print("Deja connecting")

        except BaseException as e:
            print(e)
            sleep(1)
            self.test_connecttion()

    def insert_tag(self):
        query = "INSERT INTO tag(Name_tag,Value_Tag,Type_Tag,adress,id_DB) VALUES (%s,%s,%s,%s,%s)"
        try:
            self.test_connecttion()
            val = (self.NameTag, self.Value, 2, "MB25",1)
            cursor=self.var_connection.cursor()
            cursor.execute(query,val)
            self.var_connection.commit()
            print("Success Add Tag")
        except BaseException as e:
            print(e)
        self.var_connection.close()


obj = tag("temp",bytearray(),3,"",1)
obj.insert_tag()





