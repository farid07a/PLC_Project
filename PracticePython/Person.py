class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def _print_propriety(self):
        print("name:", self.name)
        print("Age", self.age)


Person01 = Person("farid", 15)
Person02 = Person("dibouce", 30)
Person01._print_propriety()
Person02._print_propriety()

