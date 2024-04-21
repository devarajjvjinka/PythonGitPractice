tuple1 = (1, 2, 3, 4, 5, 1, 2, 3)

#for loop
for tu in tuple1:
    print(tu)

print("while loop")
count=0

while count<len(tuple1):
    print(tuple1[count])
    count+=1

print("while loop backward")

backward = len(tuple1)-1
while backward>=0:
    print(tuple1[backward])
    backward-=1




