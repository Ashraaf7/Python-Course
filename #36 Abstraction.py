from abc import ABC , abstractmethod

class Vehicle:
    @abstractmethod
    def moveForward(self):
        pass

    @abstractmethod
    def moveBackward(self):
        pass

    @abstractmethod
    def turnLeft(self):
        pass

    @abstractmethod
    def turnRight(self):
        pass

class Car(Vehicle):
    def moveForward(self):
        print('Press N')

    def moveBackward(self):
        print('Press R')

    def turnLeft(self):
        print('Press N w emshy shemal')

 
    def turnRight(self):
        print('Press N w emshy yemen')


class Moto(Vehicle):
    def moveForward(self):
        print('hat 1 w emshy')

    def moveBackward(self):
        print('No way , make it with your legs')

    def turnLeft(self):
        print('hat 1 w emshy shemal')

 
    def turnRight(self):
        print('hat 1 w emshy yemen')

car = Car()
moto = Moto()

car.moveForward()
car.moveBackward()
car.turnRight()
car.turnLeft()

moto.moveForward()
moto.moveBackward()
moto.turnRight()
moto.turnLeft()