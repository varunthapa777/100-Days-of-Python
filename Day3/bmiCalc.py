
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight/(height**2)

abs_bmi = round(bmi)

if bmi < 18.5:
    print(f"Your BMI is {abs_bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {abs_bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {abs_bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {abs_bmi}, you are obese.")
else:
    print(f"Your BMI is {abs_bmi}, you are clinically obese.")
    