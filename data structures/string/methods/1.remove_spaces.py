#  To remove spaces from string we use following methods
# 1.rstrip(): remove spaces from right side of the string
#2.lstrip(): remove spaces from left side of the string
#3.strip(): remove spaces from  both sides of the string


name="    siom"
print(name)
print(name.lstrip())
print("--------------------------------------------------")
print("right side space")
name="siom             "
for x in name:
    print(x)
print("--------------------------------------------------")
name=name.rstrip()
for x in name:
    print(x)

print("remove spaces form both side")
name= "            sinhgad             "
name=name.strip()
print(name)

