var = int(input("Please enter number : "))

if var < 0 :
    print("Entered number is less than 0")
elif var == 0 :
    print("Entered number is zero")
elif 0 < var <= 100 :
    print("Entered number 1 or in between 1 to 100")
else :
    print("Entered number is greater than 100")