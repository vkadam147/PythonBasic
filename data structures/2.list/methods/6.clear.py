'''
    6.list.clear():
        1.It will remove all elements from the list and list  becomes empty
        2. it will not remove list from memeory
        3.if we use del keyword then only that list is removed from the memory
'''
l1=[1,2,3,4,5]
print(l1)
l1.clear()
print(l1)# list is empty now

del l1 #NameError: name 'l1' is not defined
# print(l1) 
