# A simple program to make a simple calculator

a = int(input("Enter the number:"))
b = int(input("Enter the number:"))

c = input("Select the operator(+,-,*,/,%):")

if c =='+':
    print("The addition of the number is :", a+b)

elif c =='-':
    print("The subtraction of number is :", a-b)
elif c=='*':
    print ("The multiplication of the number is:",a*b)
elif c=='/':
    print("The division of the number is :", a/b)
elif c == '%':
    print("The modulus of the number is:",a%b)
else:
    print("Invalid Input!")