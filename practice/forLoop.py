str = "hello"


for char in str:
    print(char)


#find the length of the givrn string

usr_input = input("Please enter the string to find the length")
count=0
for char in usr_input:
    count+=1


print("Entered string is "+usr_input +" and lenght is " , count)