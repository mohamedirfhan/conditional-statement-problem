month = int(input("Enter a month Number: "))

if month < 1 or month > 12:
    print("Invalid month Number!!!")

elif month == 2:
    year = int(input("Enter a year: "))
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f"The {month}nd month number of days in {year} is 29")
    else:
        print(f"The {month}nd month number of days in {year} is 28")

elif month in [1, 3, 5, 7, 8, 10, 12]:
    print(f"The {month}th month number of days is 31")

else:
    print(f"The {month}th month number of days is 30")