def is_perfect(num):
    sum=0
    a=1
    while  a<num:
        if num%a==0:
            sum=sum+a
        a=a+1
    return sum==num

for x in range(6,1001):
    if is_perfect(x):
        print(x)

# without using function

# for x in range(1,1001):
#     sum=0
#     a=1
#     while a<x:
#         if x%a==0:
#             sum+=a
#         a+=1
#     if sum==x:
#         print(x)




    