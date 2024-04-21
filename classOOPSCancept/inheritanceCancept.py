from class2 import Class2


# from and import are the keyword , class1example.py is the python file name , class1 is the class name inside the class1example .py file

class class2(Class2):  # we have to mention the class name inside the paranthesis for imporing the properies.

    num2 = 200  # variable in class2

    def __init__(self):  # current class constructor
        Class2.__init__(self, 2, 3)

    # super class constructor , if we declared super class constructor explicitly , then we have to declare the super class constructor inside the chile class constructor.

    def sum(self):
        return self.num2 + self.num1 + self.func2()  # num2 is current class variable , #num2 and func2() is super class variable and method. We can access parent class properties using the self keyword.


s

# creating current class object to access method

Obj = class2()
print(Obj.sum())