# l=[1,1,2,2,3,4,5,6,6]
# unique_list=[]
# for i in l:
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list)
 
# a=[1,2,3,4,5,6]
# data=7
# b=[0]*(len(a)+1)
# for i in range(len(a)):
#     b[i]=a[i]
# b[len(a)]=data
# print(b)


# list_num=[1,1,5,1,4,1,2,5,3,2,4]
# new_list=[]
# removed=False
# for x in list_num:
#     if not removed and x==4:
#          removed=True
#          continue
#     new_list.append(x)

# print(new_list)
# a=range(20)
# print(range(20))

# max_num=sec_max=list_num[0]
# for i in list_num:
#     if i>max_num:
#         sec_max=max_num
#         max_num=i
#     elif i>sec_max and i!=max_num:
#         sec_max=i
# print(max_num,sec_max)



print("---------------------------------------------")
stack=[]
def push(data):
    stack.append(data)
    print(f"pushed:{data}")

def pop():
    if isempty():
        print("stack is empty")
        return
    data=stack.pop()
    print(f"poped:{data}")
    return data

def peek():
    if isempty():
        print("stack is empty")
        return
    data=stack[-1]
    print(f"peeked:{data}")
    return data

def isempty():
    return len(stack)==0

def size():
    return len(stack)

def display():
    for x in stack[::-1]:
        print(x,end="------>")
    print("\b\b")

def reverse():
    rev=''
    while not isempty():
        rev=rev+pop()
    return rev

# def isplaindrome(s):
#     stack1=[]
#     s=s.lower()
#     for x in s:
#         stack1.append(x)
#     for x in stack1:
#         push(x)
#     rev=reverse()
#     return s==rev


# push('vaishnavi')#puhsed:vaishnavi
# push('kadam')#pushed:kadam
# push('sinhgad')#pushed:sinhgad
# push('pune')#pushed:pune
# display()# pune---->sinhgad---->kadam---->vaishnavi---->
# peek()#peeked:pune
# pop()# poped:pune 
# display()#sinhgad---->kadam---->vaishnavi---->
# print(isempty())#false
# print(size())#3


#reverse string using stack
push('R')
push('E')
push('S')
push('T')
push('A')
push('P')
push('I')
print(isempty())
display()
print("---------------------------------------")
print(reverse())

# if isplaindrome('Madam'):
#     print("String is palindrome")
# else:
#     print("String is not palindrome")



list=['California','Austria','Denmark','Amstradam']
new_list=[x[0] for x in list]
print(new_list)


