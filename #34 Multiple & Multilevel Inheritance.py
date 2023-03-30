'''
class CollegeData: 
    def __init__(self,name, collegeId , age ):
        self.name = name
        self.collegeId = collegeId
        self.age = age 

    def displayCollegeData(self):
        print("Member Name: " + self.name + " Member Age: " + self.age )

class HostelData: 
    def __init__(self, hostelId , roomNumber ):
        self.hostelId = hostelId
        self.roomNumber = roomNumber

    def displayHostelData(self):
        print("Member ID: " + self.hostelId + " Room Number: " + self.roomNumber )

class Student(CollegeData,HostelData):
    def __init__(self,name, collegeId , age,hostelId , roomNumber ,grade):
        CollegeData.__init__(self,name, collegeId , age)
        HostelData.__init__(self,hostelId , roomNumber)
        self.grade = grade

student1 = Student('Ahmed','1','22','127','508',3.2)
student1.displayCollegeData()
student1.displayHostelData()
'''
class Vehicle:
    def __init__(self,shape):
        self.shape = shape
    
class Land(Vehicle):
    def __init__(self,shape,numberOfTires):
        Vehicle.__init__(self,shape)
        self.numberOfTires = numberOfTires

class Car(Land):
    def __init__(self,shape,numberOfTires,name):
        Land.__init__(self,shape,numberOfTires)
        self.name = name

car1 = Car('SUV','4','BMW')
print(car1.shape)