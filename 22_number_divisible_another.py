# A simple program to check weather a number is divisible by another or not

# Solution 1: Using for loop

for i in range(1,100):
    if i%12==0:
        print("The number divisible by 12 is:",i)


# Solution 2 : using lambda and filter 

l = []
num_elements = int(input("Enter the number of elements: "))

for i in range(num_elements):
    element = int(input("Enter element: "))
    l.append(element)

print(l)


result = list(filter(lambda x : x % 12==0 , l))
print(" The number divisible by 12 are : " , result)