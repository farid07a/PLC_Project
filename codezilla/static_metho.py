class math:



    # static method not use self and not cls
    # now static method cannot change any instance attribute an
    # and no access and no change the class attribute
    # it uses one or many  parameter

    @staticmethod
    def add(x,y):
        return x+y
    @staticmethod
    def add5(num):
        return num+5

    @staticmethod
    def add10(num):
        return num + 10

    @staticmethod
    def PI():
        return 3.14

x = math.add(5,10)
y = math.PI()
v = math.add5(10)
z = math.add10(100)

print(x,y,v,z)


