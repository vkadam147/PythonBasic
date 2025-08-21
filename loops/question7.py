# Find the largest among three numbers.

a=int(input("enter first num "))
b=int(input("enter second num "))
c=int(input("enter third num "))
if a>b and a>c:
    print("a is largest")
elif b>c:
    print("b is largest")
else:
    print("c is largest")
