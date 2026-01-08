days = int(input("Enter a total days:"))

years = days//365
days = days % 365

month = days // 30
days = days % 30

print("Years =",years)
print("Month =",month)
print("Days =",days)
