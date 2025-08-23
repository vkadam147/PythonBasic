# Function with Default Parameters in Python

# In Python, we can assign default values to function parameters.
# Default arguments are always assigned from **right to left**.
# That means you cannot put a non-default parameter after a default one.

def sum(a=0, b=0):   # 'a' and 'b' both have default values as 0
    return a + b

# Example Calls:
c = sum(10, 20)      # Both arguments provided -> a=10, b=20
print(c)             # Output: 30

print(sum(10, 201))  # Both arguments provided -> a=10, b=201
# Output: 211

print(sum())         # No argument provided -> a=0, b=0
# Output: 0

print(sum(5))        # One argument provided -> a=5, b=0 (default)
# Output: 5


# ❌ Wrong way (will give SyntaxError)
# def func(a=0, b):  # Cannot have a non-default after default
#     return a+b
