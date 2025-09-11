def calculator(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a//b
    return sum,sub,mul,div

sum,sub,mul,div = calculator(50,10)
print(sum,sub,mul,div)

# for x in calculator(50,10):
#     print(x)

# # Tuple
# print(type(calculator(50,10)))