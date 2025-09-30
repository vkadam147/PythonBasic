# # created list of 5 animals
animals=['Lion','Tiger','Cow','Elephant','Zebra']

#delete zebra from the list
animals.remove('Zebra')
for animal in animals:
    print(animal)
 #op=['Lion','Tiger','Cow','Elephant']


#print alternate elements from given list
for i in range(0,len(animals),2):
    print(animals[i])


# add horse to the list

animals.append('Horse')
for animal in animals:
    print(animal)


ip=['a','b',2,43,'Hi',900,'xyz']

op=[x for x in ip  if  str(x).isdigit()]

print(op)

# Write a Python program to accept a list of integers from the user and create a new list containing only the even numbers using list comprehension.

nums=[]
# created list of integers from the user
n=int(input("Enter How many numbers u want to insert in list"))
for i in range(n):
    ip=int(input("Enter Number:\n"))
    nums.append(ip)

new_list=[x for x in nums if x%2==0]
print(new_list)