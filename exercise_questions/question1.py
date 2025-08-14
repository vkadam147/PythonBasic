# write a program to take two numbers from the user and print:
#  - Sum
#  - Difference
#  - Product
#  - Quotient (normal and floor division)
#  - Remainder

num1=int(input("Enter first Number:"))
num2=int(input("Enter second Number:"))

sum=num1+num2
print(f"{num1} + {num2} = {sum}")

difference=num1-num2
print(f"{num1} - {num2} = {difference}")

if num2==0:
    print("no can't divide by zero")

else:
    quotient=num1/num2
    
    #this is normal division
    print(quotient)

    floor=num1//num2
    
    print(floor)

    remainder=num1%num2
    #modulous
    print(remainder)

