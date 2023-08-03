class Sample:
    a = 10
    b = 28
    def m1(self):
        print("mi function")

obj1 = Sample()
print(obj1.a+obj1.b)
obj1.m1()

class add:
    a = 30
    b = 40
    def addi(self):
        c = a+b
        print(c)
obj = add
print(obj.a)
print(obj.b)
obj.addi()