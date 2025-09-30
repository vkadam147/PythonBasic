# ) Write a Python program to take a tuple of numbers and return a new tuple with only unique elements and its length.

#tuple is immutable created using () or tuple() 
t=(1,2,3,1,4,5,2,3)

unique=tuple(set(t))
print(unique)
print(f"Length of tuple is {len(unique)}")


# operations on tuple
'''
    1.concatenation (+)
    2.repetation (*)
'''

#methods
'''
    1.tuple.count(data): returns frequnecy of data in tuple
    2.tuple.index(data) : returns an index of data from tuple
'''
t1=(1,2,3)
t2=(4,5,6)
# concatenation
t3=t1+t2
print(t3)

#repetation
t4=t1*2
print(t4)


#methods
print(t.count(1))
print(t.index(4))

#creating empty tuple

empty=tuple()


#create single elment tuple
one_value=(1,)
print(type(one_value))

#packing and unpacking

details=('Vaishnavi',24236,'MCA-C')
name,roll_no,div=details
print(f"Name:{name}\nRoll No:{roll_no}\nDivision:{div}")
print("--------------------------------------------")
# print(details[0])
# print(details[1])
# print(details[2])

for d in details:
    print(d)
print(type(details))
print(type(name))
print(type(roll_no))
print(type(div))



