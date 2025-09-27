# 4.Generate prime numbers between 1–50 using list comprehension. 
def is_prime(num):
    for i in range(2,num):
        if num%i==0: 
            return False
    return True


prime_numbers=[x for x in range(1,50) if is_prime(x)]
print(prime_numbers)