# A simpe program for finding the largest numbers among three numbers

a = int(input("Enter the first number: "))
b= int(input("Enter the second number: "))
c = int(input("Enter the third number: "))


if a>b and a>c:
    print("a is greatest")
elif b>a and b>c:
    print("b is greatest")
elif c>a and c>b:
    print("c is greatest")
else:
    print("all numbers are equal")