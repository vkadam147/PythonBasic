# String is data type in python
# STring is collection  or sequence of charcters written in single,double or tripple quotes
#String is immutable in python
# immutable means that we can not change onec we created


name="vaishnavi"
print(f"Type: {type(name)}")

name1='vaishnavi'
name2="vaishnavi"
name3='''vaishnavi is from wardha'''
name4="""python is interpreted language"""
print("Single quote:",name1)
print("Double Quote:",name2)
print("Tripple Quote:",name3)
print("Tripple Quote:",name4)

# Iteration of string characters using for loop
for x in name:
    print(x)

# Iteration of string using index
# index always strats from 0

for  x in range(0,len(name)):
    if x%2==0:
        print(name[x])

#negative index

print("Negative indexes:-------------")
print(name[-9])
print(name[-8])
print(name[-7])
print(name[-6])
print(name[-5])
print(name[-4])
print(name[-3])
print(name[-2])
print(name[-1])

# how to delete object in python
# we can delete object from memory using del keyword in python

a="siom"
print("Before deleting")
print(a)
del a
print("AFter deleting")
# print(a)

b="SIOMM"
print(b)
b=None
print(b)

name="abc"
print(name[3])

