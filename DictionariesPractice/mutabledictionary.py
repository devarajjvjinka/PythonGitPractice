#dictionaries and lists are mutable we can change the assigned values

dic1= {"hello":"hai","hai":"hello",1:2,1.2:5.5,3:4}
dic2 =dic1  #both dic are pointing to the same and have the same address
dic2[1]=10

print(dic2)
print(dic1)

print(len(dic2))  #prints the length of the dictionary(combination of key and value pairs