basic=int(input("Enter your Basic salary: "))

if basic<=10000:
    hra=basic*0.20
    da=basic*0.80
elif basic<=20000:
    hra=basic*0.25
    da=basic*0.90
else:
    hra=basic*0.30
    da=basic*0.95
gross=basic+hra+da
print(f"Basic salary is {basic}")
print(f"HRA is {hra}")
print(f"DA is {da}")
print(f"Gross salary is {gross}")