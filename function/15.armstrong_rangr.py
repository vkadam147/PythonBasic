def is_armstrong_no(num):
    sum=0
    temp=num
    while num!=0:
        rem=num%10
        sum=sum+(rem**3)
        num=num//10
    return temp==sum
start=int(input("enter start"))
end=int(input("enter end"))

for i in range(start,end):
    if is_armstrong_no(i):
        print(i)
