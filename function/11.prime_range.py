start=1
end=10
for i in range(start,end+1):#range giving no
    flag=True
    for j in range(2,i):#checking prime
        if i%j==0:
            flag=False
            break
    if flag:
        print(i)
           
    

    
    