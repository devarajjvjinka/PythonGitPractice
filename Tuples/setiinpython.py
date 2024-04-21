#Set wont allow duplication if item and have only one copy if we have duplicate
#set is sorted

set1 = {1, 2, 3, 4, 5, 1, 2, 3} #litteral way of declaring the set
print(set1)

set2 = set({3, 4, 5, 6, 6, 7})
print(set2)

set3 = {2, 3, 4, 5, True , "Hello"}

print(set3)

#set cannot be accessed from the index and can be accessed only from loop

for setitem in set1 :
    print(setitem)


#we can also check that element present in the set using if and in

if "Hello" in set3:
    print("Hello preent")
else:
    print("Hello not present")