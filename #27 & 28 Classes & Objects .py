class Car:  #class
    def __init__ (self,name,color,price,speed):  #constructor   
        self.name = name           #self >> ref current object
        self.color = color
        self.price = price          #Instance Attributes
        self.speed = speed

car1 = Car('BMW','Black',1000000,200)   #Object - instance
'''
        car1.name = BMW
        car1.color = Black
        car1.price = 1000000
        car1.speed = 200
'''
car2 = Car('Fiat','White',20000,50)
'''
        car2.name = Fiat
        car2.color = White
        car2.price = 20000
        car2.speed = 50
'''
print(car1.name + ' '+ car1.color + ' ' + str(car1.price))
print(car2.name + ' '+ car2.color + ' ' + str(car2.price))