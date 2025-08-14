#to check if two variables refer to the same object in memory (not just if they have the same value).
#is → True if both variables are the same object.
#is not → True if both variables are not the same object.

a=5
b=5
print(id(a))
print(id(b))
print(a is b)

x=5
y='5'
print(id(x))
print(id(y))
print(x is y)

d=5
c=5
print(id(d))
print(id(c))
print(d is c)