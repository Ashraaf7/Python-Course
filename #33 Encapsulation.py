'''
class Car :
    def __init__ (self,name,fuel):
        self.__name = name
        self.__fuel = fuel
        self.maxFuel = 70
     # Setter - Getter
    def setFuel(self,fuel): #1000 >> (70-20 = 50 liter)
        if (self.__fuel < self.maxFuel):
            fuel= self.maxFuel- self.__fuel #50
            self.__fuel += fuel
        else:
            print("Your fuel is filled")  

    def getFuel (self):
        return self.__fuel
    

car1 = Car('BMW',20)
car1.setFuel(1000)
print(car1.getFuel())
'''

class Bank:
    def __init__ (self, cardHolder , CVV , balance):
        self.cardHolder = cardHolder
        self.CVV = CVV
        self.__balance = balance


    def setBalance (self,newBalance):
        Name= input('Enter you Name: ')
        CVV =input('Enter your CVV: ')
        if (self.cardHolder == Name and self.CVV == CVV):
            self.__balance += newBalance
        else:
            print('Transiction Failed')

    def getBalance (self):
        Name= input('Enter you Name: ')
        CVV =input('Enter your CVV: ')
        if (self.cardHolder == Name and self.CVV == CVV):
            return self.__balance 
        else:
            print('Transiction Failed')

user = Bank('Ahmed' , '233' , 10000)

user.setBalance(10000)


print(user.getBalance())
