class Car:                                        #class

    numberOfCars = 0                            #class Attribute

    def __init__ (self,name,color,price,speed=200):  #constructor   
        self.name = name           #self >> ref current object
        self.color = color
        self.price = price          #Instance Attributes
        self.speed = speed
        Car.numberOfCars += 1 

car1 = Car('BMW','Black',1000000)   #Object - instance    #1
car2 = Car('Fiat','White',20000,60)   #Object - instance   #2
car3 = Car('28','Blue',10000,20)                         #3
car4 = Car('Tyota','Red',1000000,40)                         #4

print(Car.numberOfCars)