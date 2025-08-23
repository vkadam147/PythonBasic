def is_perfect(num):
    sum=0
    a=1
    while a<num:
        if num%a==0:
            sum=sum+a
        a=a+1
    return sum==num

start=int(input("enter start"))
end=int(input("enter end"))
count=0
for i in range(start,end):
    if is_perfect(i):
        
        print(i)
        count=count+1
    print(count)
    


