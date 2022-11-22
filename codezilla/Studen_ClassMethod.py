from datetime import date
# Class Method
# decorator is change the behavior of function without
# change the code of function
# @classmethod

class Student:

    def __init__(self, name, age=0, course=None):
        self.__name = name
        self.__age = age
        self.__course = course

        # this is instance attributes

    def describe(self):
        print(f"My name is {self.__name} and my age {self.__age} ")
        print("My name is {} and my age {} ".format(self.__name, self.__age))

    def get_course(self):
        return self.__course

    # this called decorator
    # class method not use parameter self
    # use parameter class (name of class)
    # while class method not it 's not use self not cannot access to instance attribute
    # but class method can acccess and change the class attribute
    @classmethod
    def init_from_birth_year(cls,name,birth_year):
        return cls(name,date.today().year-birth_year)

    def describe(self):
        print(f"My name is {self.__name} and my age is : {self.__age}")


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    @classmethod
    def veg(cls):
        return cls(["mushrooms","olives","onions"])

    @classmethod
    def margharita(cls):
        return cls(["mozzarella", "sauce"])

    def __str__(self):
        print(f"")

pza1 = Pizza(["meat"])
pza2 = Pizza.veg()
pza3 = Pizza.margharita()
print(pza1, pza2, pza3)

print(dir(Pizza))

# dundre function


student1=Student("farid", 30, ["java"])
student1.describe()

student2=Student.init_from_birth_year("ahmed",1989)
student2.describe()

print(student2.get_course())


