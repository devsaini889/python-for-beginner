# Swaping two variables using third variable

x = 12
y = 13 

temp = x          #making a third variable
x=y               #assign value of x to y 
y =temp            #storing the value of y to temp

#The value is swapped
print(x)
print(y)



# Swaping two variables without using third variable

x=12
y=13

x,y=y,x

print(x)
print(y)