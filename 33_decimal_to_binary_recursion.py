


def binary(n):
    if n>1:
        binary(n//2)

    print(n%2, end='')


print("The binary conversion of the number is: ")
binary(15)

