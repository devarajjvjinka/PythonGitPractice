print("".join(["one", "two", "three"])) # "" is a separator
print(" ".join(["one", "two", "three"])) # " " is a separator  , join will be separated by space

print(",".join(["one", "two", "three"])) #separate by ,
print("..".join(["one", "two", "three"])) #separate by ..
print(", ".join(["one", "two", "three"])) #separate by ,

print("-----")

print("Hello, world, welcome".split())
#by default split will consider space for separation

print("Hello, world, welcome".split(",")) #split by ,

print("Hello, world, welcome".split(" ")) #split by space

print("Hello, world, welcome".split(", ")) #split by ', '

