#perfect number
num=6
sum_of_divisor=0
for i in range(1,num):
    if num%i==0:
        sum_of_divisor+=i
if sum_of_divisor==num:
    print("perfect num")
else:
    print("not perfect no")

