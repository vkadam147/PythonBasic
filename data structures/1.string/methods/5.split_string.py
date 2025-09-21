para="Python is high level language which is used for data science"
words=para.split()
# for w in words:
#     print(w)
print(words)
print(type(words))
date="24-02-2003"
newDate=date.split("-")
for num in newDate:
    print(num)

joiningDate="18/03/2026"
new_joining_date=joiningDate.split("/")
print(new_joining_date)
for x in new_joining_date:
    d=int(x)
    if d%2==0:
        print(d)

mobileNo="+918888888888"
newMobileNo=mobileNo.split("+91")
print(newMobileNo)

 


