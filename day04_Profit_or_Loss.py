cp = float(input("Enter a cost price :"))
sp = float(input("Enter a selling price :"))

if sp > cp:
    print("Profit =",sp-cp)
elif cp > sp:
    print("Loss =",cp-sp)
else:
    print("No profit, No loss.")
