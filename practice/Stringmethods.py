print("Alphabetical string".isalpha())
# returns false bcz string contains  string and space
#If there are any special characters (such as punctuation
# marks or spaces) in the string, it will return False
print("--------")
print("Alphabetical".isalpha()) #returns true
print("AlphaNum123".isalnum()) #returns true
print("1234".isnumeric()) #returns true
print("2541.12".isdecimal()) #return false
print("--------")
print(" ".isspace()) #returns true
print("        ".isspace()) #returns true
print("Hi Devaraja , Welcome To Python Learning."[2].isspace()) #returns true , at index 2 , we have space
print("--------")
print("hello".istitle()) #returns false
print("Hello".istitle()) #returns true

print("hi devaraja , welcome to python learning.".title()) #returns string with first letter as capital
#Hi Devaraja , Welcome To Python Learning.




