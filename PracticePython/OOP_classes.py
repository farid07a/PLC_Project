class myClass:
    propriety = 0

    @staticmethod
    def Comparator(a, b) -> int:
        """

        :rtype: object
        """
        max = 0
        if a>b:
            print("A is Big than B")
            max = a
        else:
            print("")
            max = b
        return max


obj1 = myClass()
maxValue = myClass.Comparator(5, 6) # static values 
print(maxValue)

Obj2 = myClass()
