'''
class Math:

    @staticmethod
    def Add2(x,y):
       return x+y 
    
    @staticmethod
    def Add3(x,y,z):
       return x+y+z 
    
    @staticmethod
    def Sub2(x,y):
       return x-y 
    
    @staticmethod
    def Sub3(x,y,z):
       return x-y-z 
    
print(Math.Sub3(20,5,5))
'''

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @staticmethod
    def Compare (object1,object2):
        if isinstance(object1,Person) and isinstance(object2,Person):
            if object1.name == object2.name and object1.age == object2.age:
                print('Person1 equals Person2')
            else:
                print('Person1 NOT equal Person3')
        else:
            return NotImplemented

person1 = Person('ahmed',22)
person2 = Person('ahmed',22)
person3 = Person('ali',50)
x=5 
y=10
Person.Compare(person1,person3)