# Joining of Strings in Python
# ----------------------------
# We can join a group of strings (list or tuple) using a given separator.
# Syntax:
#     s = separator.join(group_of_strings)
#
# - separator: The string placed between elements (e.g., space, comma, dash).
# - group_of_strings: A list or tuple containing only string elements.

# Example 1: Using a tuple
t = ('sunny', 'bunny', 'chinny')

# Join with '-' separator
s = '-'.join(t)
print("Example 1 Output:", s)   # Output: sunny-bunny-chinny

# Example 2: Using a list
names = ["Ram", "Shyam", "Mohan"]

# Join with different separators
print("\nExample 2 Outputs:")
print("Space separator:", " ".join(names))      # Ram Shyam Mohan
print("Comma separator:", ",".join(names))      # Ram,Shyam,Mohan
print("Stars separator:", "***".join(names))    # Ram***Shyam***Mohan

# Example 3: Joining characters of a string
word = "HELLO"
print("\nExample 3 Output:", "-".join(word))    # H-E-L-L-O

# Important Note:
# All elements in the list/tuple must be strings.
# If they are not, convert them using str().
