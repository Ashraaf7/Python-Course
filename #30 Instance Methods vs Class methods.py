'''
class Car:                                        #class

    numberOfCars = 0                            #class Attribute

    def __init__ (self,name,color,price,speed=200):  #constructor   
        self.name = name           #self >> ref current object
        self.color = color
        self.price = price          #Instance Attributes
        self.speed = speed
        Car.numberOfCars += 1 

    #instance method
    def move (self,method):  #Manual - Automatic
        print (self.name + ' moves ' + method)

    
    def Toot(self):
        print(self.name + ' toots')


car1 = Car('BMW','Black',1000000)      
car2 = Car('128','Blue',10000,20)     

car1.move('Automatic')
car2.move('Manual')
car1.Toot()
car2.Toot()
'''

class Factory:

    #personal sizes
    def __init__ (self,size):
        self.size = size

    @classmethod
    def Small(cls):
        return cls('S')
    
    @classmethod
    def Medium(cls):
        return cls('M')
    
    @classmethod
    def Large(cls):
        return cls('L')
    
    @classmethod
    def X_Large(cls):
        return cls('XL')

Tshirt1 = Factory.Medium()
Tshirt2 = Factory.X_Large()
Tshirt3 = Factory.Large()
Tshirt4 = Factory('XXXXL')

print(Tshirt1.size + ' ' +Tshirt2.size + ' ' +Tshirt3.size + ' ' +Tshirt4.size  )
