# ---------------------------------------------------
# List Comprehension in Python
# ---------------------------------------------------

# Theory:
'''
List comprehension is a concise way to create lists in Python.
It allows looping, filtering, and transforming elements in a single line.

Syntax:
    [expression for item in iterable if condition]

Components:
1. expression  -> Operation to perform on each element (e.g., x**2, x.lower()).
2. item        -> Variable representing each element in the iterable.
3. iterable    -> Any Python iterable (list, range, tuple, etc.).
4. condition   -> Optional filter to include only certain elements.

Advantages:
- Shorter and more readable than standard for-loops.
- Often faster as it is optimized internally.
- Combines looping, condition, and expression in one line.
- Ideal for simple transformations and filters.

Execution Order:
1. Take one element from the iterable.
2. Check the condition (if present):
    - True → evaluate expression, add to result list.
    - False → skip element.
3. Repeat until all elements are processed.
'''

# ---------------------------------------------------
# Examples
# ---------------------------------------------------

# 1️⃣ Squares of numbers 0–9
squares = [x**2 for x in range(10)]
print("Squares:", squares)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 2️⃣ Cubes of even numbers 0–9
cubes = [x**3 for x in range(10) if x % 2 == 0]
print("Cubes of even numbers:", cubes)

# Output: [0, 8, 64, 216, 512]

# 3️⃣ Convert to lowercase only if string starts with 'S'
names = ['SIOM', 'SPUNE', 'RAICSIT', 'WARDHA']
lower_list = [x.lower() for x in names if x.startswith('S')]
print("Lowercase names starting with 'S':", lower_list)
# Output: ['siom', 'spune']

# ---------------------------------------------------
# Manual Implementation (for comparison)
# ---------------------------------------------------
# lower_manual = []
# for x in names:
#     if x.startswith('S'):
#         lower_manual.append(x.lower())
# print(lower_manual)
# Output: ['siom', 'spune']

# ---------------------------------------------------
# Summary / Notes
# ---------------------------------------------------
'''
- Use list comprehension for concise, readable, and fast code.
- Avoid using it for very complex logic; normal loops are clearer then.
- Filters (if condition) allow selective inclusion of elements.
- Can be used with strings, numbers, tuples, lists, and more.
'''

# ---------------------------------------------------
# Optional: Visual Execution Flow (ASCII)
# ---------------------------------------------------
'''
Example: [x**2 for x in range(3) if x%2==0]

Flow:
range(3) → [0,1,2]
Step 1: x=0 → 0%2==0 → True → 0**2 → add 0
Step 2: x=1 → 1%2==0 → False → skip
Step 3: x=2 → 2%2==0 → True → 2**2 → add 4
Result → [0,4]
'''
