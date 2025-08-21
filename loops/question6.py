#  Check if a number is armstrong
num=int(input("enter a no "))
arm=0
temp=num
while num!=0:
    rem=num%10
    arm=arm+(rem**3)
    num=num//10
if temp==arm:
    print("arm")
else:
    print("not arm")
