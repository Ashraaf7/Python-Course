age = input("Enter your age ")

if int(age) > 0:   #valid
    if int(age) > 18:
        if int(age) >18 and int(age)<60:
            print("Welcome to website")     
    else: #18 or less than 18
        print("You are underage")

else:  #0 or -
    print("Invalid age")