
class Pizza:
    def __init__(self,radius, ingredients):
        self.ingredients = ingredients
        self.radius=radius


    @classmethod
    def veg(cls):
        return cls(["mushrooms","olives","onions"])

    @classmethod
    def margharita(cls):
        return cls(["mozzarella", "sauce"])

    def __str__(self):
        return f"Pizza ingredients are {self.ingredients}"

    def area(self):
        return Pizza.circle_area(self.radius)

    # use this method to calculate data without attributes
    # static method called helper method or utility methods
    # static cannot change the Instance and Class
    @staticmethod
    def PI():
        return 3.14

    @staticmethod
    def circle_area(r):
        return r ** 2 * Pizza.PI()


class Dates:
    def __init__(self,date):
        self.__date=date

    def getDate(self):
        return self.__date
    @staticmethod
    def toDashDate(date):
        return date.replace("/","-")


date = Dates("10/10/2022")
datefromDB = "11/11/2022"
datewithDash=Dates.toDashDate(datefromDB)

if date.getDate()==datewithDash:
    print("")
else:
    print("Not Equal")





pizza = Pizza(5, ['Tomatoes', 'Fromage'])
print(pizza.area())

print(Pizza.circle_area(20))