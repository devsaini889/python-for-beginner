# A simple program to print the multiplication table

num = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{num} * {i} = {num*i}")