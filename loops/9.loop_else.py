# ============================
# if-else, for-else, while-else in Python
# ============================

# ---------- IF-ELSE ----------
# if-else is used for decision making.
# If condition is True -> if block runs
# If condition is False -> else block runs

x = 10
if x > 5:
    print("if-else Example: x is greater than 5")  # Runs because condition is True
else:
    print("x is not greater than 5")


# ---------- FOR-ELSE ----------
# for-else means:
# The 'else' part runs ONLY if the loop finishes normally (no break)
# If we use 'break', else part will NOT run

for ch in "python":
    print(ch)
    if ch == "h":
        break   # Loop stopped in middle
else:
    print("for-else Example: Loop finished without break")  # Skipped

# Another case without break
for ch in "java":
    print(ch)
else:
    print("for-else Example: Loop finished normally")  # Runs


# ---------- WHILE-ELSE ----------
# while-else is similar to for-else.
# Else block runs only if the loop ends normally (condition False)
# If loop is stopped with break, else will NOT run

count = 1
while count <= 3:
    print("Count =", count)
    count += 1
else:
    print("while-else Example: Loop ended normally")  # Runs here

# With break
count = 1
while count <= 3:
    print("Count =", count)
    if count == 2:
        break   # Stopped forcefully
    count += 1
else:
    print("This will not run because loop ended with break")


# ---------- SUMMARY NOTES ----------
# if-else → choose between 2 options based on condition
# for-else → else runs only if loop finishes without break
# while-else → else runs only if loop finishes without break
