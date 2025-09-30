#created an empty set with set() function
ip_set=set()

# add only (a-z) or (A-Z) or (0to 9)
n=int(input("Enter How many ELments u want to insert in set\n"))
for i in range(n):
    word=input("Enter Word\n")
    if word.isalnum():
        ip_set.add(word)

print("----------------------------------------")
# display all set elements

for word in ip_set:
    print(word)


# length of set

print(f"Length of set is{len(ip_set)}")



digits=lowecase=uppercase=0

for word in ip_set:
    for ch in word:
        if ch.isupper():
            uppercase+=1
        elif ch.islower():
            lowecase+=1
        elif ch.isdigit():
            digits+=1
print(digits,uppercase,lowecase)

