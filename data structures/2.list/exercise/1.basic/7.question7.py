# 7. Implement a program to find the maximum and minimum element in a list without
# using the built-in max() or min() functions.
l=[9,5,2,9,1,3,41,1,222,111]
max_num=sec_max=min_num=sec_min=third_max=l[0]

for x in l:
    if x>max_num:
        third_max=sec_max
        sec_max=max_num
        max_num=x
    elif x>sec_max:
        third_max=sec_max
        sec_max=x
    elif x>third_max:
        third_max=x
print(f"first maximum:{max_num}")
print(f"second max:{sec_max}")
print(f"third max:{third_max}")
