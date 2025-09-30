ip=['Ajay','Vijay','Ganesh','Paresh','Mahesh','Akash','Ashsih','Akay']

op=[name[0] for name in ip]

print(op)

#using list comprhension conevrt all names into lowercase

new_op=[name.lower() for name in ip]
print(new_op)


#using list comprhension create new list that contains only name that strats with 'A'

op=[name for name in ip if name.startswith('A')]
print(op)


new_list=[1,2,3,4,5,6,7,8,9,10]
even_num=[x for x in new_list if x%2==0]
print(even_num)


#using list comprhension generate first 50 prime numbers

def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

prime_nums=[x for x in range(1,51) if isPrime(x)]
print(prime_nums)


#calculate squares using list comprhension

a=[1,2,3,4,5,6,7,8,9,10]
sqaures=[x**2 for x in a]
print(sqaures)

even_nums=[x for x in a if x%2==0]
odd_nums=[x for x in a if x%2!=0]
print(even_nums,odd_nums)


