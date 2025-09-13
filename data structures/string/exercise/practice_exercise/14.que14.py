# 14. Write a program to check if 'listen' and 'silent' are anagrams.

w1='silents'
w2='listens'


# flag=False

# for ch in w1:
#     if ch in w2:
#         flag=True
#     else:
#         flag=False
#         break
# if flag:
#     print("anagram")
# else:
#     print("not anagram")


for ch in w1:
    if len(w1)!=len(w2):
        print("not anagram")
        break
    if ch not in w2:
        print("string is not anagram")
        break
else:
    print("string is anagram")


 

