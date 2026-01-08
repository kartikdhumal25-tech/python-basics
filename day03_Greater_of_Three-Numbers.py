a = int(input("Enter a first number :"))
b = int(input("Enter a second number :"))
c = int(input("Enter a third number :"))

if a > b and a > c:
    print("Greater number =",a)
elif b > c:
    print("Greater number =",b)
else:
    print("Greater number =",c)
