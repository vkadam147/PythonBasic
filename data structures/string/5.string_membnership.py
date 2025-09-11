# membership operators are IN and NOT IN

vowels=['a','e','i','o','u']
name="vaishnavi"

count=0
for x in name:
    if x not in vowels:
        count+=1

print(f"no of consonants {count}")


print("=================================================")
para="This is vaishnavi kadam from Sinhgad institute of management.Currently pursuing MCA"
degree="MCA"
if degree in para:
    print("yes it contains MCA")
else:
    print("Not Present")

# for x in para.split(" "):
#     if x=="MCA":
#         print("Yes it present")
#         break
#     else:
#         print("*")