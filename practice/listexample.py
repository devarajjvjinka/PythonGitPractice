list1 = [1,2,3,4,5,6,7]
print(list1)
list2 = ["hello","Hai","test","python",1.5,1,True]
print(list2)

list3 = [True ,False,False,True]
print(list3)

list4 = [[1,2,3,],["deva","raja"],[True,False]]
print(list4)

print(list("Devaraja"))
list6 = list("Devaraja")
print(list6)


#in and not in operators
print( [1,2,3] in list4) #true
print(3 in list4) #false
print(True in list3) #true
print("hello" not in list2) #false bcz list 2 have hello in it
print('e' in list("Devaraja")) #true