from abc import ABC, abstractmethod
class testabstract(ABC):
    @abstractmethod
    def m1(self):
        print ("M1")

    @abstractmethod
    def m2(self):
        print("M2")

    def m3(self):
        print(testabstract.m1)

obj1 = testabstract()
obj1.m3()
