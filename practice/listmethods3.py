list2 = ["hello","Hai","test","python",1,2,1,True]
print(list2)
print(list2.index("Hai")) #returns the hindex of the element

print(list2.index(1)) #returns the index of first appearing element

#pop method is used to remove the element from the list from Last by default
end = list2.pop()
print(list2)

#to remove the specific element we can mention the index of the lement to be removed
end = list2.pop(2)
print(list2)

