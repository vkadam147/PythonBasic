#Find factorial of a number.
num=int(input("enter a no"))
fact=1
while num!=0:
    fact=fact*num
    num=num-1
print(fact,num)
