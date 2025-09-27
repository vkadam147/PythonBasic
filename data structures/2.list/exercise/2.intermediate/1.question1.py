#1. Merge two lists and remove duplicates.
l1=[1,2,3,4,5,6,7,3,3,3,3,3,3]
l2=[3,4,5,6,7,8,9,10]
l1.extend(l2)
print(l1)
l3=[]
for x in l1:
    if x not in l3:
        l3.append(x)
print(l3)



# using set :inbuilt class which is used to remove duplicates from  the list of(l1+l2)
unique_list=set(l1+l2)
print(unique_list)


