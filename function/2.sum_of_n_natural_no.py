def sum_of_n(start,end):
    sum=0
    while start<=end:
        sum=sum+start
        start+=1
    print(sum)
    return sum
if __name__=="__main__":
    start=int(input("enter start:"))
    end=int(input("enter end:"))
    result=sum_of_n(start,end)
    print(result)

    if result%2==0:
        print("even no")
    else:
        print("not even")






        