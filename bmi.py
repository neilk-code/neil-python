height=float(input("enter your height in meters: "))
weight=float(input("how many kilograms do you weigh? "))
bmi=weight/(height**2)
if bmi>=17 and bmi<=18.5:
    print("you have mild thinness.")
elif bmi>18.5 and bmi<=25:
    print("you have avergae BMI.")
elif bmi>25:
    print("you are overweight.")
else:
    print("you are severely underweight.")