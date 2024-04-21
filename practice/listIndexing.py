list1 = [1,2,3,4,5,6,7]
print(list1[1])
list2 = ["hello","Hai","test","python",1.5,1,True]
print(list2[0][1])
print(list2[4])

list3 = [True ,False,False,True]
print(list3[1])

list4 = [[1,2,3,],["deva","raja"],[True,False]]
print(list4[1][0])
print("Hello "+list4[1][0])

#negative index
print("negative index")
print(list4[-1]) #iterates from end of the list
list1 = [1,2,3,4,5,6,7]  #neg index is -1 is 7 , -2 is 6 and so on -7 is 1
print(list1[-5])
print(list1[-7])

print(list1[4]+5)