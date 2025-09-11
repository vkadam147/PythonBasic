# def calc(a,b):
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     div=a//b
#     return sum,sub,mul,div
# def add(num,div):
#     return num+div
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(num,div):
#     return num//div
# div(20,1000)

# print(div(num=1000,div=5))

# # res=calc(20,30)
# # # print(res)
# # for r in res:
# #     print(r)

# def greet(name="guest"):
#     print("hello",name)

# def div1(a,b=1):
#     return a//b

# print(div1(10,2))
# print(div1(10))




# greet("vaishnavi")
# greet()

def addition(a,*n,b=10):
    sum=0
    print(f"A={a}")
    print(f"B={b}")
    print(n)

    for x in n:
        sum+=x
    print(sum)
    print("-----------------------")
    

# addition() cant be called as no argument passed
addition(1)
addition(1,2)
addition(1,2,3)
addition(1,2,3,4)
addition(1,2,3,4,5)
addition(1,2,3,4,5,6)
addition(1,2,3,4,5,6,7)
addition(1,2,3,4,5,6,7,8,9,10)

