#Membership operator(IN and NOT IN): 
'''
    This Operator is used to check whether given data is present inside the list or not
'''

cars=['skoda','swift','volkswagen','audi']

print("skoda" in cars)
print("swift" in cars)
print("kia" in cars)


print("skoda" not in cars)#False
print("swift" not in cars)#False
print("kia" not in cars)#True


#slicing:
print(cars[::])#['skoda','swift','volkswagen','audi']
print(cars[::-1])
print(cars[1:-5:-1])

# update

cars[1]='Mercedes'
print(cars)

#deleting elements
del cars[0]
print(cars)
del cars
# print(cars) # NameError: name 'cars' is not defined

#del is allowed for all types of data
a="siom"
del a
# print(a) NameError: name 'a' is not defined

b=20
del b
# print(b) # NameError: name 'b' is not defined


