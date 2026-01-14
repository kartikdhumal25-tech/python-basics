numbers = [1, 2, 2, 3, 4, 4, 5]
unique = []

for x in numbers:
    if x not in unique:
        unique.append(x)

print("Without duplicates =", unique)
