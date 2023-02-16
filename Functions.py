#defination
def Add(number1 , number2): #parameters (Header)
    result = number1 +number2 #local
    return result      
                              #body
def Greeting (name , age='25'):
    print('Hello ' + name + ' Your age is: ' + age)

def GreetingLoop(*name): #1 ('Ahmed')  #2 ('Ahmed','Mohamed')  #5 ('Ahmed','Mohamed','Ali','Noor','Aya')
        for n in name:
            print('Hello ' + n)


name = "Ahmed" #global
print(name)
#calling
'''
Greeting('Ahmed','50') #required arguments
Greeting(age=25,name='Ahmed') #keyword arguments
Greeting('Ahmed') #defualt arguments
'''
GreetingLoop('Ahmed','Mohamed','Ali','Noor','Aya') #Variable length arguments


