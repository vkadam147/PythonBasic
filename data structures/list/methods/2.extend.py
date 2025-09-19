# list.extend(iterable)

#  in extend(iterable) this method new list is added at the end of an existing list and existing ls updated
# in concatenation operation new list is created not updated

l1=[1,2,3,4]
l2=[5,6,7,8]
l1.extend(l2)
#  [1,2,3,4,5,6,7,8]
#  in this l1 is updated with [1,2,3,4,5,6,7,8]

l1=[1,2,3,4]

l3=l1+l2
#  in this new list is created of l1 and l2 combine but both l1 and l2 remains unchanged

print(l3)

# the main differenc between extend and concatenate is extend updates the list and concatenation  creates new list and orignal list will not be updated it remains same

