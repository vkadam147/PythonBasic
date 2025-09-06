def is_even(num):
    if num%2==0:
        return True
    else:
        return False
    

num=int(input("enter a no:"))
if is_even(num):
    print("even no")
else:
    print("odd")