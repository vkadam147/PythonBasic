'''
1.add(x): add an element of set
2.update(iterable):add multiple element to the given set
3.remove(x):remove( raise an error if missing)
4.discard(x):remove( does not raise an error if missing)
5.pop():remove any element from the set randomly

'''

#add(x)
a={11,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
a.add(5)
print(a)

#update(iterable)
a.update([6,8,9])
print(a)

#remove(x)
a.remove(4)
print(a)
#discard(x)
# a.remove(4) # this will raise error as 4 is not prsent in set
a.discard(4)  # this will not raise any error
print(a)

#pop()
b=a.pop()
print(f"popped:{b}")
print(a)
 
