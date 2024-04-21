var = input("Enter a number : ")

if var == 5 :
    print("value enter is equal to 5")
else:  #else part
    print("value enter is not equal to 5")



#NestedIf statement

gpa = float(input("Please enter you gpa"))
accept_status = input("Please enter the acceptance status")

if gpa>=3.4:
    if accept_status=="yes":
        print("Application has been accepted by institute")
    else:
        print("Application rejected by institute")
else:
    print("Please work to increase your gpa")

