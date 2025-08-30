height=float(input("Enter your height in meters: "))
weight=float(input("Enter your weight in kilograms: "))
bmi=weight/height**2
print(f"Your BMI is {bmi:.2f}")
print("Interpret your BMI based on the following :/nUnderweight: BMI < 18.5/nNormal weight: 18.5 <= BMI < 25/nOverweight: 25,= BMI <30/nObese: BMI >= 30")
