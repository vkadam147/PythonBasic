# 2. Find the second largest element in a list.
import random
nums=[random.randint(1,100)+x for x in range(10)]
first_max=sec_max=nums[0]

for i in nums:
    if i>first_max:
        sec_max=first_max
        first_max=i
    elif i>sec_max:
        sec_max=i
print(first_max)
print(sec_max)
print(nums)
    

