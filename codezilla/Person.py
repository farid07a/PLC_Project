from datetime import date
class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display(self):
        return f"name is {self.__name} age :{self.__age} "
    @classmethod
    def initFromBirthYear(cls,name,birthYear,extra):
        return cls(name,)


class Man(Person):
    gender="Man" # class attribute must initialise static variable
    no_of_man = 0# class attribute must initialise

    def __init__(self,name,age,voice):
        super().__init__(name,age) # constructor of base class
        self.voice = voice
        Man.no_of_man += 1    # class attribute class

    def display(self):
        string_herit=super().display()
        return string_herit+ f" and my voice is {self.voice} and gender :{Man.gender} or gender by self {self.gender}"

class woman(Person):
    gender="female"
    no_of_woman = 0

    def __init__(self,name , age, hair):
        super().__init__(name,age)
        self.hair=hair

    def display(self):
        strin_msg=super().display()
        return strin_msg+f"My gender is {woman.gender} and hair{self.hair}"


wom=woman("farid",30,"curly")
print(wom.display())

wom=woman("farid",30,"curly")

print(woman.no_of_woman)





man=Man("farid",30,"nice")

print(man.display())

man1=Man("amin",40,"hard")
print(Man.no_of_man) # like static variable

