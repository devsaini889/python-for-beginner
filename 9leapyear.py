

year = int(input("Enter the year :"))

if year % 400 == 0 and year % 100 == 0 :

    print("This year is leap year")

elif year % 4 == 0  and  year % 100 != 0:
    print("The year is leap year")
else:
    print("The year is non leap year")