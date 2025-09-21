
'''
    Created an Empty stack of name stack
'''
stack=[] 

def push(data):
    stack.append(data)
    print(f"Pushed:-{data}")
    print("----------------------------------------------------------")


def pop():
    if isempty():
        print("stack is empty")
        print("----------------------------------------------------------")

    else:
        data=stack.pop()
        print(f"Popped Data is: {data}")
        print("----------------------------------------------------------")

 

def peek():
    if isempty():
        print("stack is empty")
        print("----------------------------------------------------------")

    else:
        data=stack[-1]
        print(f"Peeked: {data}")
        print("----------------------------------------------------------")


def clear():
    stack.clear()
    print("stack is cleared")
    print("----------------------------------------------------------")


def isempty():
    return len(stack)==0

def size():
    return len(stack)
def display():
    if isempty():
        print("stack is empty")
        return
    for data in stack[::-1]:
        print(data)
    print("----------------------------------------------------------")


while True:
    print("1.push\n2.pop\n3.peek\n4.clear\n5.isempty\n6.size\n7.display\n8.exit")
    ch=int(input("Enter Your Choice (1-7)"))
    if ch==1:
        data=input("Enter Data")
        push(data)
    elif ch==2:
        pop()
    elif ch==3:
        peek()
    elif ch==4:
        clear()
    elif ch==5:
        if isempty():
            print("Stack is empty")
        else:
            print("stack have elements")
            display()
    elif ch==6:
        print(f"size of the stack is {size()}")
    elif ch==7:
        display()
    elif ch==8:
        print("Thanks!!!!!!!!!!!!!!")
        break
    else:
        print("Please enter correct choice from 1 to 8")



class Stack:
    def __init__(self):
        self.stack=[]
    def push(self ,data):
        self.stack.append(data)
        print(f"Pushed:{data}")
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            data=self.stack.pop()
            print(f"Pooped:{data}")
            return data
    def peek(self):
          if self.isempty():
            print("stack is empty")
          else:
            data=self.stack[-1]
            print(f"Peeked:{data}")
            return data
    def isempty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
    def clear(self):
        self.stack.clear()
    def display(self):
        if self.isempty():
            print("stack is empty")
        else:
           return stack[::-1]
         
# a=Stack()
# a.push(10)
# a.push(20)
# a.push(30)
# a.push(40)
# a.push(50)
# a.push(60)
# a.display()
# print("------------------------------------------")
# b=Stack()
# # b.display()
# b.push(10)
# b.push(10)
# b.push(10)
# b.push(10)
# b.push(10)
# b.push(10)
# b.push(10)
# b.push(10)
# b.push(10)
# b.push(10)
# b.push(10)
# b.display()

