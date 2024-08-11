# At first we see the square root by using arithematic operatora

a=9
b=a**(1/2)
print(b)

# we can take input from the user 

a = int(input("Enter the number: "))
b= a**(1/2)
print(b)

# By second method we can import math and use its dictionary for square root

import math as m

# This comment below allow us to see the all mathematical opertion in import math 
# print(dir(m))

a = m.sqrt(4)
print(a)