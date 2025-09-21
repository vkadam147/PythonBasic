# 9. Given a list, count the frequency of each element and display the result in dictionary
# format.

l=[1,2,1,2,3,4,5,6]
a=dict()

for x in l:
    a.setdefault(x,l.count(x))

for (key,value) in a.items():
    print(key,"=",value)
