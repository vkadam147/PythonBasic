t=(1,2,3,4,5,"vaishnabi")
t1=tuple([1,2,3,4])#convert list into tuple
t2=1,2,3,4 #create tuple
t3=(1,) #single value tuple
t4=(8) #its not tuple
print(t)
print(type(t))
print(id(t))

print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])
print(t[5])

print("==========")
for x in t:
    print(x)


for i in range(len(t)):
    print(t[i])

i=0
while i<len(t):
    print(t[i],end=' ')
    i+=1
    
#slice operator
print(t[1:3])
print(t[::-1])

name="vaishnavi"
t1=tuple(name)
print(t1)

l1=list(name)
print(l1)