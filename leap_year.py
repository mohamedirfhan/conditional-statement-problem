year=int(input("Enter a year: "))
if (year%400==0)or(year%4==0 and year%100!=0):
    print(f"The {year} is Leap year")
else:
    print(f"The {year} is Not leap year")