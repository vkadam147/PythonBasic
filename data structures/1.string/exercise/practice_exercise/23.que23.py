# 23. Check if 'race car' is a palindrome (ignore spaces).

a="race car"
b=""
for ch in a:
    if not ch.isspace():
        b+=ch
print(b)

if b==b[::-1]:
    print("palindrome")
else:
    print("not palindrome")
