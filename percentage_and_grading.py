ph=int(input("Enter your physics mark: "))
che=int(input("Enter your chemistry mark: "))
bio=int(input("Enter your biology mark: "))
math=int(input("Enter your mathematics mark: "))
com=int(input("Enter your computer mark: "))
total=ph+che+bio+math+com
percentage=total/5

if ph<35 or che<35 or bio<35 or math<35 or com<35:
    print("Fail!!")
    print(f"The total mark is {total}")
    print(f"The percentage is {percentage}")
else:
    if percentage>=90:
        grade="A"
    elif percentage>=80:
        grade="B"
    elif percentage>=70:
        grade="C"
    elif percentage>=60:
        grade="D"
    elif percentage>=35:
        grade="E"
    else:
        grade="F"
    print("Pass!!")
    print(f"The total mark is {total}")
    print(f"The percentage is {percentage}")
    print(f"The grade is {grade}")