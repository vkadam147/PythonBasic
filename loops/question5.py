#  Check if a number is palindrome.

num=int(input("enter a no "))
reverse=0
temp=num
while num!=0:
    rem=num%10
    reverse=reverse*10+rem
    num=num//10
print(reverse)
print(num)
if temp==reverse:
    print("palindrom")
else:
    print("not palindrom")




