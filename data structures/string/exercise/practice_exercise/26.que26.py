# 26. Replace multiple spaces with a single space in 'Python is awesome'.

a="python     is           awesome"
list=a.split()
# print(list)

b=" ".join(list)
print(b)