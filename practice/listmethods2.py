list1 = [1,2,3,4,5,6,7]

list2 = ["hello","Hai","test","python",1.5,1,True]

list2.append("test") #appends the element at the end of the list
print(list2)

list2.insert(2,"automation") #inserts the element at the specified index
print(list2)

list3 = [5,8,7,2,6,3,1]
list3.sort()
print(list3)

# list2.sort() #sort cant be done bcz list have multiple types
# print(list2)

list3.sort(reverse=True) #sorts the list in reverse order
print(list3)

#sort does not use alphabetical order , instead it uses ASCII betical order
#capital later comes first later small letters


example_asciiBetical =["king","King","Test","test"]
example_asciiBetical.sort()
print(example_asciiBetical)

#to get the list order by alphabetical order use key=str.lower
example_asciiBetical.sort(key=str.lower)  #o/p  ['King', 'king', 'Test', 'test']
print(example_asciiBetical)