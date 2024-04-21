from ast import slice

list1 = [1,2,3,4,5,6,7]
list2 = [[1,2,3,],["deva","raja"],[True,False]]

#List slicing is used to fetch the specific part of the list

print(list1[:3]) #displays the elements from 0 to 2
print(list1[3:6])

print(list2)
print(list1[3:]) #from the index 3 to remaining all elements will be printed.