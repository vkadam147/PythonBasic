# start=1
# end=101
# for i in range(start,end):
#     flag=False
#     for j in range(2,i):
#         if i%j==0:
#             flag=True
#             break
#     if not flag:
#         print(i)
    
def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
print(is_prime(23))
start=1
end=10
for i in range(start,end):
    if is_prime(i):
        print(i)

print(is_prime(10233))

