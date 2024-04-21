dic1= {"hello":"hai","hai":"hello",1:2,1.2:5.5,3:4}

print("hello" in dic1.values())  #returns true

#if and else statements in dic

if "hello" in dic1 :
    print(dic1["hello"]+" present in dictionary")
else:
    print("helloa key is not present in the dictionary")


#istead of if and else statement we can use get() method to get the same result
print(dic1.get("helloa","helloa not present in the dictionary"))
print(dic1.get(1,"1 not present in the dictionary"))