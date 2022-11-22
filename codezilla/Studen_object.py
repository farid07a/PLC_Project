from codezilla.Student import Student

student1=Student("Farid",30,["java"])

student1.name="new instance attribut add in object student1"
print(student1.name)
student1.__name="new instance attribut with __name  add in object student1"
print(student1.__name)

print(student1.get_name())
print(student1.get_age())
print(student1.get_courses())

student1.age=77 # add new attribute name age not __age
print(student1.get_age()) # return value of __age

# print(student1.__age) because private