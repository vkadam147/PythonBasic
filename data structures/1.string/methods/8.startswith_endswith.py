
# Checking Starting and Ending Part of a String in Python
# -------------------------------------------------------
# Python provides two built-in methods for this:
#
# 1) s.startswith(substring)  → Checks if string starts with given substring
# 2) s.endswith(substring)    → Checks if string ends with given substring
#
# Both methods return True if condition is satisfied, otherwise False.

# Example string
s = 'learning Python is very easy'

# 1) startswith()
print("1) startswith() examples:")
print(s.startswith('learning'))   # True (string begins with 'learning')
print(s.startswith('Python'))     # False (string does not begin with 'Python')

# 2) endswith()
print("\n2) endswith() examples:")
print(s.endswith('learning'))     # False (string does not end with 'learning')
print(s.endswith('easy'))         # True (string ends with 'easy')

# ------------------------------------------------------------
# Summary (for quick revision):
# ------------------------------------------------------------
# Method              | Example                                    | Output
# ------------------- | ------------------------------------------ | ------
# s.startswith("sub") | "hello world".startswith("hello")          | True
# s.startswith("sub") | "hello world".startswith("world")          | False
# s.endswith("sub")   | "hello world".endswith("world")            | True
# s.endswith("sub")   | "hello world".endswith("hello")            | False
