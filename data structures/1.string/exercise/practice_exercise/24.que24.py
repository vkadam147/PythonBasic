# 24. Count the occurrences of each character in 'mississippi'.

a="mississippi"
b=[]

for ch in a:
    b.append(ch)
#print(b)
set=set(b)
#print(set)
for ch in set:
    print(f"{ch}={b.count(ch)}")
    