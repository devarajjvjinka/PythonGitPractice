global_Variable = "Global variable - declared of out the function"

def func():
    global_Variable = "Local variable - declared with in the function"
    print(global_Variable)


print(global_Variable)
print(func())

#local variables can not be accessed out side of the function means in global level

def func1():
    local = "local variable value"


#print(local) #invalid , error displays

#global variables can be accessed inside the function
def func2():
    print(glob)

glob ="glob variable"
print(func2())

# same variable name can be used within functions and outside of the function as global variable



#changing value of the global variable in function  as local variable
def func3():
    fruit = "Pear"
    print(fruit)

def func4():
    fruit = "Apple"
    print(fruit)


fruit = "Watermelon"
func3()
func4()
print(fruit)


#accessing the global variable and assiging new value in function as local variable

var = "global value"
def func5():
    var = "changing value og global variable in function"
    print(var)


print(var)
print(func5())

#assigning new value to global variable inside function
var = "global value"

def func6():
    global var
    var = "changing value of global variable in function"
    print(var)


print(func6())
print(var)