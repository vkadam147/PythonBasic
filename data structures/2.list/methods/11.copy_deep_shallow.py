# Notes on Shallow Copy vs Deep Copy IMP for interview

# Example List
l1 = [1, 2, 3, 4, [5, 6, 7]]
print(id(l1[4]))

# ---------------- SHALLOW COPY ----------------
l2 = l1.copy()
print(id(l2[4]))   # shallow copy

print("Before shallow copy change:")
print("l1:", l1)
print("l2:", l2)

# Change inner list
l1[4].append(8)

print("\nAfter shallow copy change:")
print("l1:", l1)   # inner list changed
print("l2:", l2)   # inner list also changed because both share same inner object

# ---------------- DEEP COPY ----------------
import copy
l3 = copy.deepcopy(l1)   # deep copy

print("\nBefore deep copy change:")
print("l1:", l1)
print("l3:", l3)

# Change inner list
l1[4].append(9)

print("\nAfter deep copy change:")
print("l1:", l1)   # changed
print("l3:", l3)   # unchanged, because deep copy makes its own copy of inner objects

# ---------------- NOTES ----------------
"""
Shallow Copy:
- Creates a new outer list
- Inner mutable objects (like list, dict) are shared
- Changes in nested objects reflect in both

Deep Copy:
- Creates a completely new copy of outer list
- Also copies all nested objects
- Changes in nested objects do NOT affect the other list
"""
