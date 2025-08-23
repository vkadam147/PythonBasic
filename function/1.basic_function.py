"""
📘 Functions in Python – Notes with Examples
--------------------------------------------

🔹 What is a Function?
- A function is a block of code that performs a specific task.
- It can be reused multiple times.
- Functions make code modular, readable, and reusable.

👉 Think of a function like a machine:
   - You give input (parameters).
   - It processes something.
   - It may or may not return an output.

--------------------------------------------
🔹 Types of Functions
1. Based on Parameters:
   a) Parameterized Function  → takes input
   b) Non-Parameterized Function → no input

2. Based on Return Value:
   a) Function with return  → sends back result
   b) Function without return → just performs a task

--------------------------------------------
🔹 How to Create a Function
Syntax:
    def function_name(parameters):
        # function body
        return value   # (optional)

Optional parts:
    1. Parameters
    2. Return statement
"""

# ------------------------------------------------
# 1. Non-Parameterized Function (No input, No return)
# ------------------------------------------------
def greet():
    """This function takes no input, prints greeting message"""
    print("Hello, welcome to Python Functions!")

# Calling the function
greet()

print("--------------------------------------------------")

# ------------------------------------------------
# 2. Parameterized Function (Takes input, Returns result)
# ------------------------------------------------
def add(a, b):
    """This function takes two numbers and returns their sum"""
    return a + b

sum_of_two = add(10, 20)
print("Sum =", sum_of_two)        # using variable
print("Direct Call:", add(100, 200))  # direct call

print("--------------------------------------------------")

# ------------------------------------------------
# 3. Function without Return (Only prints result)
# ------------------------------------------------
def print_numbers(start, end):
    """This function prints numbers from start to end"""
    while start <= end:
        print(start, end=" ")
        start += 1
    print()  # for newline

print("Numbers from 1 to 5:")
print_numbers(1, 5)

print("--------------------------------------------------")

# ------------------------------------------------
# 4. Function with Return (Returns value for later use)
# ------------------------------------------------
def square(n):
    """This function returns square of a number"""
    return n * n

print("Square of 5:", square(5))
x = square(10)
print("Square of 10:", x)

print("--------------------------------------------------")

# ------------------------------------------------
# Real Life Analogy
# ------------------------------------------------
"""
👉 Function is like:
- Calculator Button:
    You press 'Add' with two numbers → you get sum.
- ATM Machine:
    Insert card (parameter), enter PIN (parameter) → you get cash (return value).
"""

# ------------------------------------------------
# 🔹 Summary Table (for notes)
# ------------------------------------------------
"""
| Function Type                   | Input (Parameter) | Return Value | Example                 |
|---------------------------------|-------------------|--------------|-------------------------|
| Non-parameterized, no return    | ❌                | ❌           | greet()                 |
| Parameterized, no return        | ✅                | ❌           | print_numbers(1,5)      |
| Non-parameterized, with return  | ❌                | ✅           | get_pi() → 3.14         |
| Parameterized, with return      | ✅                | ✅           | add(10,20) → 30         |
"""
