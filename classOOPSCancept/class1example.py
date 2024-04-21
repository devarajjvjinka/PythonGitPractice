class class1:
    num = 100

    def __init__(self):
        print("constructor will be executed first before all the things in the class ")


    def func1(self):  #function inside the class
        print("first class")


obj = class1() #oject creation ,
# in python no need of using new keyword to create the object
obj.func1() #calling function present inside the class using class object
print(obj.num) #printing the value present inside the class using object.