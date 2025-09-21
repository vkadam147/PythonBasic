'''
    9.list.sort()
     1.it will sort the given list in natural order
     2.natural order means ascending or alphabetical
'''
l1=['a','x','b','c','a','d']
l1.sort()
print(l1)

l2=[22,221,-1,2,1,0]
l2.sort()
print(l2)


# list.sort(reverse=True):this will sort in descending order or simply reverse the ascending list
l3=[0,123,2,3111,4,5,6]
l3.sort(reverse=True)
print(l3)

l4=[0,123,2,3111,4,5,6]
l4.sort()
l4.reverse()
print(l4)