def armstrong_no(num):
    arm=0
    temp=num
    while num!=0:
        rem=num%10
        arm=arm+(rem**3)
        num=num//10
    return temp==arm
a=armstrong_no(151)
print(a)
if a:
    print("armstrong no")
else:
    print("not armstrong")






































