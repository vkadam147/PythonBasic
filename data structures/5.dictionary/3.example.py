# a) Create a dictionary containing any 5 elements in the form of key,
# value pair, and write python code to perform the following operations
# on it.
# i) To display all the keys.
# ii) To add new key value pair.
# iii) To delete specific element from the dictionary.
# iv) To modify value of a particular key.

# created dictionary of 5 keys and value
week={
    'sunday':'python',
    'monday':'Java',
    'Tueseday':'AWS',
    'Wednesday':'Linux',
    'Thurseday':'Apache Kafka'
}

# display all the keys

for key in week.keys():
    print(key)

# To add new key value pair in dictionary
week['Friday']='SpringBoot'
print(week)

# deleting specific element from ditionary

del week['Friday']
print(week)

week.pop('monday')
print(week)

# Modifying particular value from dictionary

week['Tueseday']='Java'
print(week)