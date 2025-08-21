start=int(input("enter a start:"))
end=int(input("enter end"))
count=0
sum=0
while start<=end:
   if start%2==0:
    sum=sum+start

    count=count+1
    print(start)
   start = start+1
print(f"no of even{count} ")
print(f"sum={sum}")