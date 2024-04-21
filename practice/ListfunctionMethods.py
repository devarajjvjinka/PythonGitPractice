list1 = [1,2,3,4,5,6,7]

list2 = ["hello","Hai","test","python",1.5,1,True]
#delete is a function to remove the element from the list
del list1[0]
del list2[6]
print(list1)
print(list2)

#remove function is also do the same function as like delete
print("remove")
list1.remove(6)
print(list1)
list2.remove("python")
print(list2)

list3 = [1,2,3,4,5,1,2,3,4,"deva","deva","raja"]
list3.remove("deva") #even though we have multiple matching in the list ,
# remove function removes the first matching
list3.remove(1)
print(list3)



