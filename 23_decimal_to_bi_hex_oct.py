# A simple program to convert a decimal to binary ,hexadecimal and octal

deci= int(input("Enter the number in decimal:"))

# To covert the decimal we have python builtin function 

print("The decimal number is:", deci)
print(bin(deci) , "in binary")
print(hex(deci),"in hexadecimal")
print(oct(deci) ,"in octal")