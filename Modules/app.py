import Modules.use_fuc
import use_fuc
from Modules.use_fuc import roll_dice


print(Modules.use_fuc.roll_dice(20))
print(roll_dice(10))


from Modules.Employee import Employee

from Employee import Student


emp=Employee("farid",20,"Computing Science",True,200)
emp.bonus()

emp=Student("student",25,35,"major","univ biskra")

print(emp.name)