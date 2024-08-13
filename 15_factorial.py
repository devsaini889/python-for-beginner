# A simple program to generate factorial of number

def factorial(m):
    if m == 0:
        return 1
    else:
        return m * factorial(m - 1)

n = int(input("Enter the number: "))
a = factorial(n)
print(a)


# Second method to calculate the factorial


n = int(input("Enter the number:"))
fact = 1
if n<0:
    print("factorial does not exits")
elif n==0:
    print("factorial is 1")
elif n>1:
    for i in range(1,n+1):
        fact=fact*i
print("factorial of given numberis:",fact)