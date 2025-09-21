# 6. Write a Python program to create a list of integers and calculate the sum of all
# elements without using the built-in sum() function.

l=[x for x in range(11)]
sum=0
for x in l:
    sum=sum+x
print(sum)



