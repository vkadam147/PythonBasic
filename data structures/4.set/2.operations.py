
'''
    we can perform following operations on set
        1.union (|)
        2.Intersection (&)
        3.difference(-)
        4.symmetric difference (^)

    1.Union(|):
        merging of two sets
    2.Intersection(&):
        common elements of two sets
    3.difference(-):
        1 (a-b): n Python, the set difference operation returns a new set containing all the elements that are present in the first set (A) but not in the second set (B).

    4.symetric difference(^)
        (a^b):common elements of a and b are removed and remaining are returned
'''
a={1,2,3}
b={3,4,5,6}

#union(|)
print(a|b)

#intersection(&)
print(a&b)

#difference(-)
print(a-b)                        

#symmetric_difference(^)
print(a^b) #remove common element of two sets and merge two sets