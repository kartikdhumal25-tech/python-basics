numbers = [10, 45, 2, 89, 23]

max_num = numbers[0]
min_num = numbers[0]

for x in numbers:
    if x > max_num:
        max_num = x
    if x < min_num:
        min_num = x

print("Maximum =", max_num)
print("Minimum =", min_num)
