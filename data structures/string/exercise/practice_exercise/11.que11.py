# 11. Reverse the string 'OpenAI'.

a='OpenAI'
b=a[::-1]
print(b)
d=""
c=len(a)-1
while c>=0:
    d+=a[c]
    c-=1
print(d)
e=""
for ch in a:
    e=ch+e;

print(e)



