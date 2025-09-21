# 3. Count even and odd numbers in a list.

a=[1,2,4,4,5,6,7,8,9,10]
even_count=0
odd_count=0
for x in a:
    if x%2==0:
        even_count+=1
    else:
        odd_count+=1
print(f"even count={even_count}")
print(f"odd count={odd_count}")

 