def sum_of_digits(num):
    sum=0
    while num!=0:
        rem=num%10
        num=num//10
        sum=sum+rem
    return sum
a=sum_of_digits(9529134122)
print(a)

