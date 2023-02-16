#defination
def Calculator(number1,number2,operation): #add - subtract - multiply
    if operation == 'add':
        print(int(number1)+int(number2))
    elif operation == 'subtract':
        print(int(number1)-int(number2))
    elif operation == 'multiply':
        print(int(number1)*int(number2))
    else:
        print('Invalid operation')

def Sum(*numbers): #1    1,2    1,2,3
    sum = 0 #6   #local
    for number in numbers:
        sum += number
    print(sum)  
    

#calling
'''
Calculator('100','50','add')
Calculator('100','50','subtract')
Calculator('100','50','add')
Calculator('100','50','subtract')
Calculator('100','50','multiply')
Calculator('100','50','subtract')
Calculator('100','50','subtract')
Calculator('100','50','multiply')
Calculator('100','50','multiply')
'''
Sum(1,2,3,4,5)