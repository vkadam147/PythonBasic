def reverse_no(num):
    reverse=0
    while num!=0:
        rem=num%10
        num=num//10
        reverse=reverse*10+rem
    return reverse

num=int(input("enter a no"))
a=reverse_no(num)
print(a)
num=int(input("enter a no"))
a=reverse_no(num)
print(a)























































