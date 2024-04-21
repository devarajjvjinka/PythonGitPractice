dic1= {"hello":"hai","hai":"hello",1:2,1.2:5.5,3:4}

print(dic1.keys()) #prints the keys presents in the dictionary

#we can also iterate using for loop

for key in dic1.keys() :
    print(key)

print("-----")
#we can also use value() method to get all the values present in that dictionary
print(dic1.values())

#iterationg using for loop
for value in dic1.values():
    print(value)


print("items() method return the key and values in the parathesis format")

print(dic1.items())

#we can also iterate it using for loop
for key, value in dic1.items() :
    print(key ,"-", value)
   # print(key); print(value)

print(type(dic1.keys()))
print(type(dic1.values()))
print(type(dic1.items()))

print(list(dic1.keys()))  #returns the key present in dic
print(list(dic1.values())) #returns the value present in dic
print(list(dic1.items())) #returns the key and values present in dic