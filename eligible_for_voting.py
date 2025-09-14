age=int(input("Enter your Age= "))
if age<=0:
    print(f"Enter your proper age!")
elif age>=18:
    print(f"you are eligible to vote")
else:
    print(f"you are not eligible to vote")