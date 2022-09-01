import math
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"your bmi is {bmi} you are under weight.")
elif bmi < 25:
    (f"your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"your bmi is {bmi}, you are over weight.")
elif bmi < 35:
    print(f"your bmi is {bmi}, you obese.")
else:
    print(f"your bmi is {bmi}, you are clinically obese.")
