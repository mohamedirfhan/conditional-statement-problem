a=int(input("Enter a number of day in week: "))
if a>=7:
    print("Enter the correct day!")
elif a==1:
    print(f"the {a} day is Monday")
elif a==2:
    print(f"the {a} day is Tuesday")
elif a==3:
    print(f"the {a} day is wednesday")
elif a==4:
    print(f"the {a} day is thursday")
elif a==5:
    print(f"the {a} day is friday")
else:
    print(f"the {a} day is saturday")