# Changing Case of a String in Python
# -----------------------------------
# Python provides built-in methods to change the case of characters in a string.

# 1) upper()       → Converts all characters to UPPERCASE
# 2) lower()       → Converts all characters to lowercase
# 3) swapcase()    → Converts lowercase → UPPERCASE and UPPERCASE → lowercase
# 4) title()       → Converts string to Title Case 
#                    (first letter of each word capital, rest lowercase)
# 5) capitalize()  → Converts only the first character of the string to uppercase
#                    and the rest to lowercase

# Example string
text1 = "python programming"
text2 = "hELLO wORLD"
text3 = "PyThOn"

# 1) upper()
print("1) upper()")
print("Original:", text1)
print("Uppercase:", text1.upper())   # Output: PYTHON PROGRAMMING

# 2) lower()
print("\n2) lower()")
print("Original:", text2)
print("Lowercase:", text2.lower())   # Output: hello world

# 3) swapcase()
print("\n3) swapcase()")
print("Original:", text3)
print("Swapcase:", text3.swapcase()) # Output: pYtHoN

# 4) title()
print("\n4) title()")
print("Original:", text1)
print("Title Case:", text1.title())  # Output: Python Programming

# 5) capitalize()
print("\n5) capitalize()")
print("Original:", text2)
print("Capitalize:", text2.capitalize()) # Output: Hello world

# Summary Table (for quick revision)
# ----------------------------------
# Method        | Description
