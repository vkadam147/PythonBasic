# 18. Print the frequency of each word in 'python is fun and python is powerful'.


sent='python is fun and python is this powerful'
a=sent.split(" ")
 
b=set(a)
print(a)
print(b)
for word in b:
    print(f"{word}: ",a.count(word))
    