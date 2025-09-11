def sum(*a):
    print(type(a))
    print(f"a:{a}")
    sum=0
    for x in a:
        sum+=x
    print(f"sum:{sum}")

sum()
sum(1)
sum(1,2)
sum(1,2,3)

