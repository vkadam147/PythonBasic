def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
if isprime(72):
    print("prime")
else:
    print("not prime")


num=13
flag=True
for i in range(2,num):
    if num%i==0:
        flag=False
        break
if flag:
    print("prime")
else:
    print("not prime")

