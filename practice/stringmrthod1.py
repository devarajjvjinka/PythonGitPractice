str = "hello convert to upper"
print(str.upper()) #converts to upper case

str1 = "HELLO CONVERTS TO LOWER."
print(str1.lower()) #converts to lower case
print("--------")
print(str1.isupper()) #returns true .
print("".isupper()) #returns false
print("".islower()) #returns false
print(str.islower()) #returns true .
print("--------")
print("Hello world".isupper()) #returns false
print("!@#!@#".isupper()) #returns false
print("!@#123A".isupper()) #returns true  given string should have atleast one char for comparision
print("--------")
print("Hello world".islower()) #returns fasle
print("HELLO".islower()) #returns false
print("123!@#a".islower()) #returns true
print("$100 is the bill".islower()) #returns true

