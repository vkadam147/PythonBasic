def perfect_no(num):
    a=1
    sum=0
    while a<num:
        if num%a==0:
            sum=sum+a
        a=a+1
    return sum==num
if perfect_no(6):
    print("perfect")
else:
    print("not perfect")
# a=perfect_no(6)
# print(a)
# if a:
#     print("perfect no")
# else:
#     print("not perfect")
