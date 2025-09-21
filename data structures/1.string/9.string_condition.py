# Truthy and Falsy Values in Strings
# ----------------------------------
# In Python, strings are treated as boolean values in conditions:
#
# - Any NON-EMPTY string → Treated as True
# - EMPTY string ("")   → Treated as False
#
# This is very useful in if-else conditions.

# Example 1: Non-empty string
n = "vaishnavi"

if n:   # condition is True because string is not empty
    print("if block executed")
else:
    print("else block executed")

# Example 2: Empty string
n = ""

if n:   # condition is False because string is empty
    print("if block executed")
else:
    print("else block executed")

  

# ------------------------------------------------------------
# Summary (for quick revision):
# ------------------------------------------------------------
# Value       | Treated as | Example Result
# ----------- | ---------- | ------------------------
# "hello"     | True       | if "hello": executes if block
# " " (space) | True       | if " ": executes if block
# "" (empty)  | False      | if "": executes else block
