unit=int(input("Enter your electric unit: "))
if unit<=0:
    print(f"Invalid unit!!")
else:
    if unit<=50:
       charge=(unit*0.50)/20*100
    elif unit>50 and unit<=150:
       charge=(unit*0.75)/20*100
    elif unit>150 and unit<=250:
       charge=(unit*1.20)/20*100
    else:
       charge=(unit*1.50)/20*100
    print(f"The {unit} unit charge is {charge}")