# 4. Reverse a list without using the reverse() method.

a=[3,1,1,3,4,2]
size_a=len(a)-1
size_b=0
b=[0]*len(a)

while size_a>=0:
    b[size_b]=a[size_a]
    size_b+=1
    size_a-=1
print(b)

