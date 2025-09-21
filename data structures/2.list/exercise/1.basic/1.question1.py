# 1 Create a list of the first 10 natural numbers and print their squares.

# using list comprhension

a=[x**2 for x in range(11)]
print(a)
#  without using list comprhension using normal loop
a=[]
for x in range(11):
    a.append(x**2) #this will append square of each number from range x=0 to x=10
print(a)