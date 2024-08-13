# A simple program for checking the prime number in an interval

import random as r

num = r.randint(2,100)
print(num)

if num ==1:
    print("The number is not a prime number")
elif num>1:
    for i in range(2,num):
        if num%i==0:
            print("The number is not prime number")
            break
        else:
            print("The number is prime number" )
            break