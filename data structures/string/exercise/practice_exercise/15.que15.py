# 15. Extract only the digits from 'Order123 placed on 14-09-2025'.


order='Order123'
d=""
for x in order:
    if x.isdigit():
        d+=x
print(d)



#cocunt no of digits no of alphabets and no of symbols in vaishnavi@19

password='Vaishnavi@19'
digit=alpha=symbols=upper=lower=0

for x in password:
    if x.isdigit():
        digit+=1
    elif x.isalpha():
        alpha+=1
        if x.isupper():
            upper+=1
        else:
            lower+=1
    else:
        symbols+=1
print(f"no of digits:{digit} no of alphabets:{alpha} upper:{upper} lower:{lower} no of symbols:{symbols}")
    

