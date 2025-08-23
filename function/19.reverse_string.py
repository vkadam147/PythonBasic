def reverse_string(name):
    rev=""
    l=len(name)-1
    while l>=0:
        rev=rev+name[l]
        l=l-1
    print(rev)
reverse_string("vaishnavi")
