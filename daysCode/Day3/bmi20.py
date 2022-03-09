# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = round(weight / (height**2))

obesity = ""

if bmi < 18.5:
    obesity = f"Your BMI is {bmi}, you are underweight."
elif bmi < 25:
    obesity = f"Your BMI is {bmi}, you have a normal weight."
elif bmi < 30:
    obesity = f"Your BMI is {bmi}, you are slightly overweight."
elif bmi < 35:
    obesity = f"Your BMI is {bmi}, you are obese."
else:
    obesity = f"Your BMI is {bmi}, you are clinically obese."

print(obesity)
