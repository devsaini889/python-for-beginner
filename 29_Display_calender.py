# A simple program to determine the calender of a month


import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

calender = calendar.month(year, month)

print(calender)