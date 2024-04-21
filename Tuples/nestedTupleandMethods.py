nested = (1, 2, 3, (2, 2, 33, 44), (99, 65, 54), 2 , 3, 4, 1, 2)

print(nested)
print(nested[3])
print(nested[3][2])

#count method is used to count the number of times the give element is repeating
print(nested.count(2)) #number 2 repeating 3 times

print(nested[3].count(2)) #number 2 repeating 2 times

print(nested.index(2)) #index of element 2 will be returned(first appeard