# Count vowels and consonants in a string.
name="vaishnavi"
# i=0
# count=0

# while i<len(name):
#     if name[i]=='a' or name[i]=='e' or  name[i]=='i' or  name[i]=='o' or  name[i]=='u':
#         count=count+1
#     i=i+1

# print("vowels=",count)
# print("consonant ",len(name)-count)

count=0
for i in name:
    if i=='a' or i=='e' or i=='o' or i=='u' or i=='i':
        count=count+1
print("vowel",count)
print("consanant",len(name)-count)

    

