# 25. Check if two strings are rotations of each other ('abcde' and 'deabc').

a="abcde"
b="deabc"

a=sorted(a)
b=sorted(b)
print(a==b)