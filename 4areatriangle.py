# This is a program for calculating the area of triangle 


# If we didn't use the float the compiler did not do our calculation and give type error because we can 
# enter anything in the input so to differentiate this we use float datatype


b = float(input("Enter the value of base of triangle: "))
h = float(input("Enter the height of the triangle: "))

Area = (1/2)*b*h
print(Area)