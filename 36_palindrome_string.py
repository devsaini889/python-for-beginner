# A simple program to check the number is palindrome or not 

n = input("Enter a word here:")

a = n[::-1]

if a==n:
    print("The number is palindrome")

else:
    print("The number is not a palindrome")