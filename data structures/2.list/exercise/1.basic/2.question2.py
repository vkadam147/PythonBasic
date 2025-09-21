# 2. Find the largest and smallest number in a list.


a=[111,12222,13,14,15,16,1117,56,53]
max_num=a[0]
for x in a:
    if x>max_num:
        max_num=x
print(f"Maximum Number from the list is:{max_num}")

print(f"Maximum Number from the list is:{max(a)}")

min_num=a[0]
for x in a:
    if x<min_num:
        min_num=x
print(f"Minimum Number from the list is:{min_num}")

print(f"Minimum Number from the list is:{min(a)}")


# find second max and second min from the list

a=[111,12222,13,14,15,1226,17,526,53]
min_num=second_min=max_num=second_max=a[0]

for x in a:
    if x>max_num:
        second_max=max_num
        max_num=x
    elif x>second_max:
        second_max=x
    
        
print("First Max:",max_num)
print("Second Max:",second_max)

for x in a:
    if x<min_num:
        second_min=min_num
        min_num=x
    elif x<second_min:
        second_min=x
    
        
print("First Min:",min_num)
print("Second Min:",second_min)






