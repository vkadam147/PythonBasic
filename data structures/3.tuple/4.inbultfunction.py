'''
 1.len(object): returns the length of given  object
 2.max(object):return the maximum element of given iterable
 3.min(obj):return the minimum element of given iterable
 4.sum(obj):return the sum of element of given iterable
5.sorted(obj):sort the tuple into natural sorting order
6.tuple(iterable):convert interable(list,dict,set) into tuple
'''

t1=(1,2,3,4,5,0,-2,1,19,-23)
#len(obj):
print(len(t1))

#max(iterable)
print(max(t1))

#min(iterable)
print(min(t1))

#sum(object)
print(sum(t1))

#sorted(object)
print(sorted(t1))

#tuple(iterable)
x=tuple([1,2,3,4])
y=tuple({1,3,6,5})
z=tuple({1:'one',2:'two',3:'three'})
print(x,y,z)
a=1,2
b=tuple(a)
