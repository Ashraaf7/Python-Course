'''
student1  = "Boy"
student2 = "Boy"

if student1=="Boy" and not student2=="Girl":
    print("Student1 is a Boy and student2 is a Boy")


or >> 1 2 3 4 5 6
and >> 1 2 3
not >> 
'''
'''
print("-----Main Menu-----")
print("Press 1 for +")
print("Press 2 for -")
print("Press 3 for *")

numberOne = 10 
numberTwo = 20

choice = input("Enter your choice ") #string

if choice == "1":  #int >> casting or ""
    print(numberOne + numberTwo)

elif choice == "2":
    print(numberOne - numberTwo)

elif choice== "3":
    print(numberOne * numberTwo)

else:
    print("Invalid choice")
'''

age = input("Enter your age ") #string

if age < "18" :
    print("You are underage")

else:
    print("You are adult")
