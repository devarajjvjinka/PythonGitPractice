set1 = {1, 2, 3, 4, 5, 1, 2, 3}

set1.add(10)
set1.add("Deva")
print(set1)

set1.remove(3)
print(set1)

set1.discard("Deva")
print(set1)

set2=set1.copy()
print(set2)

#union to combine both sets to one
set4 = {1, 2, 3, 4}
set5 = {4, 5, 6, 7 , 3, 2}
set6 = set4.union(set5) #we can use | in place of union mrthod
print(set6)

set7 = set(range(1, 10 , 2)) #using range also we can define the elements of the sets
print(set7)

set8 =set4.intersection(set5)
print(set8)

set9 =set4 - set5 #set4 element will returns by subtracting from set5
print(set9)  #we can use differ
set10= set4.difference(set5)
print(set10s)




