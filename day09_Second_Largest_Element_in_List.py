numbers = [10, 45, 23, 89, 67]

max1 = numbers[0]
max2 = numbers[0]

for x in numbers:
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2 and x != max1:
        max2 = x

print("Second largest =", max2)
