# 27. Find all the words that start with 'p' in 'python is powerful and popular'.

a="python is powefull and popular"
b=a.split()

for ch in b:
    if ch.startswith('p'):
        print(ch)
   
