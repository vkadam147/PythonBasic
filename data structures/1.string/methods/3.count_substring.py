# count(): occurence of substring from the orignal string
#count(substring):It returns the count of given substring from orignal string

#count(substring,start,end): It returns the count of given substring from start index to end-1 index

fruit="apple"
count=fruit.count("p")
print(count)

laptop="sinhgad institute of management"

count=laptop.count('i',6,len(laptop))
print(count)
