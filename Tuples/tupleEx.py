tuple1 = (1, 2, 3, 4, 5, 1, 2, 3)
print(tuple1)
tuple2 = tuple("Devaraja")
print(tuple2)
tuple3 = (2.2, 3.5, "hello", "test", True)
print(tuple3)

#tuples value can be accessed through index
print(tuple3[2])

#tuple slicing
print(tuple1[0:])
print(tuple1[2:6])
print(tuple1[:6])
print(tuple1[2:6])
print(tuple1[2:])

#tuple step()
print("------")
print(tuple1[::2]) #prints 0th element and add index 2 prints next element
print(tuple1[1::2])
print(tuple1[6::-2]) #backward print till 6-2,

#tuple is immutable , can not be change

#we can reaasign the value to the tuples
#tuple1[0]="a" TypeError: 'tuple' object does not support item assignment
print(tuple1)
#we use tuple when we want data list unchanged through out the project
#tuples are faster and consume less space than the list
