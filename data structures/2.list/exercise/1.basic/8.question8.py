# 8. Reverse a list without using slicing ([::-1]) or the reverse() method. Explain the
# logic you used.

a=[1,2,3,4,5,6,7,8,9,10]
i=len(a)-1 # indiced of list a
b=[0]*len(a)
j=0 # indices of list b

while i>=0:
    b[j]=a[i]
    j=j+1
    i=i-1
print(b)


