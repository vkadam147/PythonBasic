# 5. Check if the string 'pythonprogramming' starts with 'python' and ends with 'ing'.

a="pythonpromming"
b=a.startswith('python')
c=a.endswith('ing')
if b:
    print(f"string starts with python ")
else:
    print("string does not starts with python")
if c:
    print("string endswith ing")
else:
    print("string does not ends with ing")
