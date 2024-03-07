# Don't change the code below
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
result = weight / height ** 2
bmi = round(result)

if result < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif result <= 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif result <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif result <= 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
