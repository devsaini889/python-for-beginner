# A simple program to determine the factorial using recursion 

def fact(n):
    if n==0 or n==1:
        return 1
    
    else:
        return (n* fact(n-1))
    


n= int(input("Enter the number :"))


if n<0:
    print("Invalid input")

else:
    print("The factorial of the number is: " ,fact(n))