#2 methods :
#Overloading >> same name  but diff signature (data type or #parameter)
#Overriding >> same name and same signature 

'''
#Overloading (polymarphism)
def Add(number1,number2):
    print(number1+ number2)

def Add(number1,number2,number3):
    print(number1+ number2+number3)

def Add(number1,number2,number3,number4):
    print(number1+ number2+number3+number4)

Add(10,20,30,40)
Add(10,20)
'''
#ovveriding
class Parent:
    def Hobbies(self):
        print('I can not play football')

class Child(Parent):
        def Hobbies(self):
          print('I can play football')

parent = Parent()
child = Child()

parent.Hobbies()
child.Hobbies()
