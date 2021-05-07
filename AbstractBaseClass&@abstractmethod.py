# Following is the syntax for defining abstract method in abstract class in Python:
# from abc import ABC, abstractmethod
# Class MyClass(ABC):
#       @abstractmethod
#       def mymethod(self):
#             #empty body
#             pass


# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth


rect1 = Rectangle()
print(rect1.printarea())
