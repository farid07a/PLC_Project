class Student:
    # can change self with other name
    # and add befor all attributs

    no_of_students = 0  # class attributes this like final attribute

    # and this use like static variable

    # use this default value when create constructor without parameter
    # and
    def __init__(self, name, age=0, course=None):
        self.__name = name
        self.__age = age
        self.__course = course
        Student.no_of_students += 1
        # this is instance attributes

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_course(self, list_course):
        self.__course = list_course

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_courses(self):
        return self.__course

    # methods
    # 3 type of methods
    # 1-instance methods use self attributes (self)
    # use self to access instance attributs
    def describe(self):
        print(f"My name is {self.__name} and my age {self.__age} ")
        print("My name is {} and my age {} ".format(self.__name, self.__age))

    def is_old(self, num):
        if self.__age <= num:
            print("Student is not old")
        else:
            print("Student id old")





std = Student("Farid", 20, ["programing"])

std.set_name("amine")
std.name = "public attr"

print(std.name)

student1 = Student("Islam", 20, ["css", "java"])
student2 = Student("farid", 30, ["python", "java", "c"])
student1.describe()
print(student1.is_old(50))
print(student1)
print(student2)

print("id1", id(student1))
print("id2", id(student2))

print(student1 == student2)

student2.name = "amine"
print(student2.name)
# display static variable
print(student2.no_of_students)
print(Student.no_of_students)
