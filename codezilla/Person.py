from datetime import date
class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display(self):
        return f"name is {self.__name} age :{self.__age} "

    # create constructor with class method
    @classmethod
    def initFromBirthYear(cls,name,birthYear,extra):
        return cls(name,date.today().year-birthYear,extra)



class Man(Person):
    gender = "Man" # class attribute must initialise static variable
    no_of_man = 0# class attribute must initialise

    def __init__(self,name,age,voice):
        super().__init__(name,age) # constructor of base class
        self.voice = voice
        Man.no_of_man += 1    # class attribute class

    def display(self):
        string_herit=super().display()
        return string_herit+ f" and my voice is {self.voice} and gender :{Man.gender} or gender by self {self.gender}"


class Woman(Person):

    gender = "female"
    no_of_woman = 0

    def __init__(self,name , age, hair):
        super().__init__(name,age)
        self.hair=hair

    def display(self):
        string_msg = super().display()
        return string_msg+f"My gender is {self.gender} and hair{self.hair} "


man = Man("Farid_constructor", 30, "hard")
print(man.display())
man = Man.initFromBirthYear("name_ClassMethod", 1989, "black")
print(man.display())

wom = Woman("women", 33, "black")

print(wom.display())

wom = Woman.initFromBirthYear("Woman", 1989, "yellow")
print(wom.display())

print(isinstance(wom,Woman))


