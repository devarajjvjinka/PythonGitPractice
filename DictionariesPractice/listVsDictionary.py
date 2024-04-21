print([1,2,3]==[3,2,1])  #false in the list eventhough
# have the same values but index is different
print([1,2,1]==[1,1,2])  #Flase

# in dictionary if we have same values in different index result will be true.

dic1= {"hello":"hai","hai":"hello",1:2,1.2:5.5,3:4}
dic2 = {"hai":"hello","hello":"hai",3:4,1:2,1.2:5.5}

print(dic1==dic2)  #result will be true

#keyError va;ue if we try to access the key that doen not present
print(dic1[5])  #KeyError: 5