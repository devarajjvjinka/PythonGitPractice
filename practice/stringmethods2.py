print("string starts with letter".startswith("string")) #returns true

print("string starts with letter".startswith("s")) #returns true

print("string starts with letter".startswith("String")) #returns false

print("string starts with letter".startswith("S")) #returns true


print("-----------")

print("string starts with letter!".endswith("letter!")) #returns true
print("string starts with letter!".endswith("!")) #returns true
print("string starts with letteR".endswith("R")) #returns true
print("string starts with letter".endswith("R")) #returns false
print("string starts with letter".endswith("l")) #returns false