class Person:
        def __init__ (self,name,age,id):
            self._name = name  #protected
            self.age = age
            self.id = id 

        def display(self):
            print(self._name + " " + self.id)

class Teacher(Person):
    def __init__(self,name, age , id ,salary):
            super().__init__ (name, age , id)
            self.salary = salary

class Student(Person) :
       def __init__(self,name, age , id ,grade):
            super().__init__ (name, age , id)
            self.grade = grade

teacher1 = Teacher('ahmed','50','1',90000)
teacher1.display()


student = Student('mohamed','20','5',2.3)
student.display()