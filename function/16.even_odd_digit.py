def even_odd(num):
    even_count=0
    odd_count=0

    while num!=0:
        rem=num%10
        if rem%2==0:
            even_count+=1
        else:
            odd_count+=1
        num=num//10
    print(f"no of even digits {even_count} no of odd digits {odd_count}")
even_odd(1232)


def add(num1,num2):
    
    return num1+num2
a=add(2,3)
print(a)