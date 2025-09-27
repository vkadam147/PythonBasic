'''
    stack:
        1.stack is linear data structure which follows LIFO (Last in First Out)
        2.In stack element is inserted  from the end (append()):-push()
        3.in remove operation last element is always removed in stack:- pop()

        stack operations:
            1.push(data): Element inserted at the end of the list
            2.pop(): last element is removed from the list
            3.peek(): last element is retrived but not removed
            4.clear(): stack (list) is cleared makes it empty not delete
            5.isempty(): it checks whether the stack is empty by using its len(list)==0
            6.size(): it returns the size of stack using [len(list)]
'''

def display(stack):
    for x in stack[::-1]:
        print(x)


stack=[]

print(stack)    
# push 5
stack.append(5)
# push 10
stack.append(10)
# push 15
stack.append(15)
# push 20
stack.append(20)
# push 25
stack.append(25)

#  for display stack
display(stack)
#pop
a=stack.pop()
print(f"Popped element is :{a}")
display(stack)

#peek()
peek=stack[-1]
print(f"peek element:{peek}")

#isempty()

if len(stack)==0:
    print("stack is empty")
else:
    print("stack have elements")

#size():
print(f"Size of stack is {len(stack)}")










































