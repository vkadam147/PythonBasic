# String data type in python is immutable once we create we can not change it in any way
#  If we perform any operation on string then new string is created not old is updated
name="siom"
print(id(name))# both name id must be differnt
name=name+" Pune"
print(id(name))
print(name)
print(name[0])
# name[0]='z'
print(name)