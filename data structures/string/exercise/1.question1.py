# Q. Write a program to access each character of string in forward and backward direction
# by using while loop

name="vaishnavi"
i=0
while i<len(name):
    print(name[i])
    i=i+1
print("-----------------------------------")
a=-1
while a>=-len(name):
    print(name[a])
    a-=1
    
print("-----------------------------------")

for x in name[::]:
    print(x)
print("-----------------------------------")

for x in name[::-1]:
    print(x)
print("-----------------------------------")


