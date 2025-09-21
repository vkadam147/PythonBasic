squares=[ x**2 for x in range(10)]
print(squares)

cubes=[x**3 for x in range(10) if x%2==0]
print(cubes)

list=['SIOM',"SPUNE",'RAICSIT','WARDHA']

# manual implementaion without comprhension
# for x in  range(len(list)):
#     list[x]=list[x].lower() 
# print(list)

# with comprhensiom
lower_list=[x.lower() for x in list if x.startswith('S')]
print(lower_list)

'''
List Comprehension Execution Order:

1. Loop starts → one element is taken from iterable
2. Condition is checked (if given)
3. If condition is True → expression is evaluated and added to result
4. If condition is False → expression is skipped
5. Repeat until loop finishes
'''
 