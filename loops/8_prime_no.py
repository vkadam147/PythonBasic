num=2
flag=False
for i in range(2,num):
    if num%i==0:
        flag=True
        break
if flag==True :
    print("not prime")
else:
    print("prime")