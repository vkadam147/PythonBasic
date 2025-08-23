# def palindrom_no(num):
#     reverse=0
#     temp=num

#     while num!=0:
#         rem=num%10
#         num=num//10
#         reverse=reverse*10+rem
# #     if temp==reverse:
#         return True
#     else:
#         return False
# a=palindrom_no(121)
# print(a)
# if a:
#     print("palindrom")
# else:
#     print("not palindrom")

def palindrom_no(num):
    reverse=0
    temp=num
    while num!=0:
        rem=num%10
        reverse=reverse*10+rem
        num=num//10
    return temp==reverse
a=palindrom_no(121)
print(a)
if a:
    print("palindrom")
else:
    print("not palindrome")














