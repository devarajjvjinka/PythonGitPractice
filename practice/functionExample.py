#always have 2 lines of gap between any statements and functions

print("hello")

#function with no parameters
def func(): #def is keyword to defind the function, fun() is a function name
    print("first function")  # statements to execute inside the function


func()  #call the function to execute.

def func(a , b):
    print(a , b)
    print(a+b)

func(1,2) #call the function to execute.

def func(num1=5 , num2=6):
    print(num1+num2)


func()  #default function ,
# if dnt pass values also , it will take default values defined in the function
func(7)
func(7,7)


#retun functionality in function

def func_return(x,y): #func_return returns x+y ,
    return x*y


result = func_return(4,5) #function return addition and result stories in result
print(result)

length = int(input("Enter an integer that represents length in feet."))
width = int(input("Enter an integer that represents width in feet."))
height = int(input("Enter an integer that represents height in feet."))


def prism_vol(l, w, h):
    return l * w * h


print("The volume of the rectangular prism is " + str(prism_vol(length, width, height)) + " cubic feet.")
