print("1111hello world , welcome111111".rstrip("1"))
print("1111hello world , welcome111111".lstrip("1"))
print("1111hello world , welcome111111".strip("1"))

print("-------")

print("eblubleuyellowblue".strip("blue"))

print("eblubleuyellowblue".lstrip("blue"))


print("eblubleuyellowblue".rstrip("blue"))


print("Hellow world , welcome".replace("welcome","Deva"))

print("Hellow world , welcome".replace(" ","Deva"))

print("-----")

the_string = "North Dakota"
print(the_string.rjust(17))
print(the_string.ljust(17, "*"))
center_plus = the_string.center(16, "+")
print(center_plus)
print(the_string.lstrip("North"))
print(center_plus.rstrip("+"))
print(center_plus.strip("+"))
print(the_string.replace("North", "South"))