def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
start=int(input("enter start"))
end=int(input("enter end"))

for j in range(start,end):
    if isprime(j):
        print(j)

