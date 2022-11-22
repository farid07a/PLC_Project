class Employee:
    def __init__(self,name,age,deparetement,is_manger,salary):
        self.name=name
        self.age=age
        self.deparetemen=deparetement
        self.is_manager= is_manger
        self.salary=salary

    def bonus(self):
        if self.age:
            self.salary+=500
            print("salary is:"+str(self.salary))
        else:
            print("No bonus")

class Student:
    def __init__(self,name,age , gpa, major, univ_name):
        self.name=name
        self.age=age
        self.gpa=gpa
        self.major=major
        self.univ_name= univ_name



