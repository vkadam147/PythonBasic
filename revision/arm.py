def is_arm(num):
    sum=0
    temp=num
    while num!=0:
        rem=num%10
        sum=sum+rem**3
        num//=10
    return temp==sum

for i in range(1,1000):
    if is_arm(i):
        print(i)
