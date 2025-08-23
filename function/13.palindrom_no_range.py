def is_palindrome(num):
    if num<=9:
        return False
    reverse=0
    temp=num
    while num!=0:
        rem=num%10
        reverse=reverse*10+rem
        num=num//10
    return temp==reverse

start=int(input("enter start "))
end=int(input("enter end "))
for j in range(start,end):
    if is_palindrome(j):
        print(j)







        