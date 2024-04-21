class Class2:

    num1 = 100;


    def __init__(self , a, b):
        self.fNum=a
        self.lNum=b
        print("initializing the constructor")


    def func1(self):
        #we have to declare function inside the class should have self as parameter by default.
        print("method 1")


    def func2(self):
        print("method 2")
        return  self.fNum + self.lNum + Class2.num1


Obj = Class2(2,3)
Obj.func1()
print(Obj.num1)

Obj = Class2(4,5)
Obj.func2()
print(Obj.num1)
print(Obj.func2())