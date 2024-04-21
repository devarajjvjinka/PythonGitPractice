list1 = [1,2,3,4,5,6,7]
list1[0]=8 #element at the index 0 will be replaced with 8
print(list1)
list1[5:8]=[5,5,5,5]   #slicing and add th eelements from index 5 and extends the list.
print(list1)


up_by_two = [[0, 2], [4, 6], [8, 10], [12, 14]]
print(up_by_two[0])
print(up_by_two[3][1])
furniture = ["chair", "table", "desk", "lamp", "bed"]
print(furniture[-5])
print("Most people own at least " + str(up_by_two[0][1]) + " " + furniture[0] + "s.")
floats = [0.98, 8.76, 6.54, 4.32]
print(floats[1:])
print(floats[1:3])
print(floats[:2])