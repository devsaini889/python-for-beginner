# A simple program to print the sum of n natural number using recurssion

def nsum(n):
    if n<=1:
        return n
    else:
        return n+ nsum(n-1)
    

n = int(input("Enter the number:"))

for i in range(n):
    print(nsum(i))