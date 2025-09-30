'''
 1.A Dictionary is collection of heterogeneous data stored in key-value pair
 2.In Python Dictionary is created using {}
 3.Dictionary is mutable (We can change)
    3.1 In dictionary keys are  immutable and values arte mutable
    3.2 We can update values in dictionary nut we cant update keys in dictionary
 4.Duplicates are not allowed for keys in dictionary
'''

'''
    1.creating dictionary
'''
student={
    'name':'shubham',
    'roll_no':24252,
    'class':'MCA-B'
}
print(student)

'''
 1.Accessing values in dictionary:
    we can access value in dictionary using dict_name[key]
2.Accessing values in dictionary using 
 dict.get(key)
'''
print(student['name']) #accessing using its key

print(student.get('roll_no')) # accessing using dict.get() method


# Iterating keys and values using for loop
for key in student:
    print(key,"==",student[key])


'''
1.Adding new key value pair in dictionary
    dict[key]=value
'''
student['college']='Sinhgad Institute Of Management'
print(student)

'''
    1.Modifying a Value:
    dict[oldKey]=newValue
'''
student['name']='Shubham Pandit Puri'
print(student)

'''
    Deleting an item
    del dict['key']--->remove key from dict
    dict.pop(key)---->remove key value-pair from dict
'''

# deleting from dictionary using del

del student['class']
print(student)

student.pop('college')
print(student)

'''
    displaying keys,values and items
'''
print(student.keys())
print(student.values())
print(student.items())

'''
    Looping Through Dictionary
'''
for key in student:
    print(key,' = ',student[key])

for value in student.values():
    print(value)


for (key,value) in student.items():
    print(key,'-->',value)


'''
    clear the dictionary
    dict.clear()
'''
student.clear()
print(student)
