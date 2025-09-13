# String Formatting in Python
# ---------------------------
# We can format strings with variable values using:
#   - Replacement operator {} 
#   - format() method
#
# There are 3 main ways:
# 1) Default order (placeholders filled in sequence)
# 2) Index-based order (placeholders filled using index numbers)
# 3) Keyword arguments (placeholders filled using variable names)

# Example variables
name = 'durga'
salary = 10000
age = 48

# 1) Default order
print("1) Default order:")
print("{} 's salary is {} and his age is {}".format(name, salary, age))
# Output: durga 's salary is 10000 and his age is 48

# 2) Index-based order
print("\n2) Index-based order:")
print("{0} 's salary is {1} and his age is {2}".format(name, salary, age))
# Output: durga 's salary is 10000 and his age is 48

# 3) Keyword arguments
print("\n3) Keyword arguments:")
print("{x} 's salary is {y} and his age is {z}".format(z=age, y=salary, x=name))
# Output: durga 's salary is 10000 and his age is 48

# ------------------------------------------------------------
# Summary (for quick revision):
# ------------------------------------------------------------
# Method            | Example                                      | Output
# ----------------- | -------------------------------------------- | ----------------------------
# Default order     | "{} 's salary is {}".format("Ram", 20000)    | Ram 's salary is 20000
# Index-based order | "{0} is {1} years old".format("Shyam", 30)  | Shyam is 30 years old
# Keyword arguments | "{x} got {y} marks".format(x="Mohan", y=95) | Mohan got 95 marks
