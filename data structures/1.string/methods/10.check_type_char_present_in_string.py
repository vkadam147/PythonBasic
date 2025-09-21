# String Character Checking Methods in Python
# --------------------------------------------
# This program demonstrates different built-in methods
# to check types of characters present in a string.

# 1) isalnum()  -> True if string has only letters and numbers
# 2) isalpha()  -> True if string has only letters (alphabets)
# 3) isdigit()  -> True if string has only digits (0-9)
# 4) islower()  -> True if all letters are in lowercase
# 5) isupper()  -> True if all letters are in uppercase
# 6) istitle()  -> True if string is in Title Case (each word starts with Capital)
# 7) isspace()  -> True if string contains only spaces

# Example strings
s1 = "abc123"
s2 = "Hello"
s3 = "12345"
s4 = "hello"
s5 = "HELLO"
s6 = "Python Programming"
s7 = "   "

# 1) isalnum()
print("1) isalnum() - Letters + Numbers")
print(s1, ":", s1.isalnum())   # True (letters+numbers)
print(s2, ":", s2.isalnum())   # True (letters only → also valid)
print(s3, ":", s3.isalnum())   # True (digits only → also valid)
print(s7, ":", s7.isalnum())   # False (only spaces)

# 2) isalpha()
print("\n2) isalpha() - Only Letters")
print(s2, ":", s2.isalpha())   # True
print(s4, ":", s4.isalpha())   # True
print(s1, ":", s1.isalpha())   # False (contains digits)

# 3) isdigit()
print("\n3) isdigit() - Only Numbers")
print(s3, ":", s3.isdigit())   # True
print(s1, ":", s1.isdigit())   # False

# 4) islower()
print("\n4) islower() - Only Lowercase")
print(s4, ":", s4.islower())   # True
print(s2, ":", s2.islower())   # False (H is capital)

# 5) isupper()
print("\n5) isupper() - Only Uppercase")
print(s5, ":", s5.isupper())   # True
print(s2, ":", s2.isupper())   # False

# 6) istitle()
print("\n6) istitle() - Title Case")
print(s6, ":", s6.istitle())   # True ("Python Programming")
print(s2, ":", s2.istitle())   # True ("Hello")
print(s4, ":", s4.istitle())   # False ("hello")

# 7) isspace()
print("\n7) isspace() - Only Spaces")
print(repr(s7), ":", s7.isspace())   # True
print(s2, ":", s2.isspace())         # False


# isalnum → letters + numbers

# isalpha → only letters

# isdigit → only numbers

# islower → only small letters

# isupper → only capital letters

# istitle → first letter capital in each word

#  isspace → only spaces