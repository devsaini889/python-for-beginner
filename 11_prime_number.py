# A simple program to check a number is prime number or not 

prime = int(input("Enter the number"))


if prime ==1:
    print("The number is not a prime number")
elif prime>1:
    for i in range(2,prime):
        if prime%i==0:
            print("The number is not prime number")
            break
        else:
            print("The number is prime number" )
            break