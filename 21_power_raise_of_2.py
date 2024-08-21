# A simple function in which we use lambda function to raise the power of two 

power = int(input("Enter the power to be raised : "))

result = list(map(lambda x: 2**x, range(power+1)))

print(result)