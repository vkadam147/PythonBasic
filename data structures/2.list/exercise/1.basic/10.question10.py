# 10. Write a program to remove duplicates from a list while maintaining the original
# order of elements.


l=[1,2,23,42,5,52,611,7,6,8,8,9,1,9,2,11,23]
unique_list=[]
for x in l:
    if x not in unique_list:
        unique_list.append(x)
print(unique_list)

 