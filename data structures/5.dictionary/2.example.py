
'''
    creating dictionary
'''

student={
    'name':'vaishnavi',
    'roll_no':24326,
    'mobile_no':9529134122
}
print(type(student))
print(student)

'''
    Accessing value in dictionary
'''
print(student['name'])
print(student['roll_no'])
print(student['mobile_no'])

'''
    2.Adding new key-value pair in dictionary
    dict_name[key]=value
'''
student['college']='SIOM'
student['college']='SCOE'

print(student)

'''
    3.Modifying the value in dictionary
    dict_name[key]=newValue
'''
student['name']='Vaishnavi Kadam'
print(student)

'''
    Deleting an key-value pair from dictionary
    1.del dict[key]
    2.dict.pop(key)
'''

del student['college'] 
print(student)

student.pop('roll_no')
print(student)

'''
    iterating dictionary
    1 dict.keys():---->keys
    2.dict.values():------>values
    3.dict.items()------->(key,value)
'''
print(type(student.keys()))
for key in student.keys():
    print(key,'--->',student[key])

for value in student.values():
    print(value)


for (key,value)  in student.items():
    print(key,"===",value)


'''
    clear():clears the dictionary
'''
student.clear()
print(student)
