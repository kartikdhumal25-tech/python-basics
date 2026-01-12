numbers = [10, 21, 4, 7, 18, 9]

even = 0
odd = 0

for x in numbers:
    if x % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even count =", even)
print("Odd count =", odd)
