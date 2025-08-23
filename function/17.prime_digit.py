def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
num1=2342
sum=0


while num1!=0:
    rem=num1%10
    if is_prime(rem):
        sum=sum+rem
        print(rem)
    num1=num1//10
print("sum=",sum)

    



