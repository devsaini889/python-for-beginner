# A simple program to print the fibonacci series 

a = 0
b = 1
num = int(input("Enter the number:"))
if num==1:
    print(a)

else:
    print(a)
    print(b)
    for i in range(2,num):
        c=a+b
        a=b
        b=c
        print(c)