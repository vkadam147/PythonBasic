# substring_methods.py
# ----------------------
# 🔍 Finding substrings in Python
# We can use these 4 methods:

text = "datascience"

# 1️⃣ find()
# - Finds the FIRST occurrence of substring.
# - Returns index if found, else -1.
print("find():")
print(text.find("sci"))   # 4
print(text.find("abc"))   # -1
print()

# 2️⃣ rfind()
# - Finds the LAST occurrence of substring.
# - Returns index if found, else -1.
text2 = "applea"
print("rfind():")
print(text2.find("a"))    # 0 (first 'a')
print(text2.rfind("a"))   # 5 (last 'a')
print()

# 3️⃣ find(substring, start, end)                                                                                                                                                                                                                      
print()

# 4️⃣ index() 
# - Works like find(), but raises ERROR if not found.
print("index():")
print(text.index("sci"))   # 4
# print(text.index("abc")) # ❌ ValueError

# try:
#     print(text.index("abc"))
# except:
#     print("above substring is not present!!!!!!!!!!!!!!!!!!!!!!!")

# print("End of program")

# rindex():
    # finds the index of the substring from right side
    #if substring not found then it will throw Valueerror

str="vaishnavi kadam is clever girl"

print(str.index('e'))#21
print(str.rindex('e')) #23

