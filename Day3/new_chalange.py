height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)
if bmi < 18.4:
    print(f"your bmi is {bmi}, you are under weight.")
elif bmi < 25:
    print(f"your bmi is {bmi}, you have A Normal weight.")
elif bmi < 30:
    print(f"your bmi is {bmi}, you are overweight")
elif bmi < 35:
    print(f"your bmi is {bmi}, you are obese")
else:
    print(f"your bmi is {bmi}, you are clinically obese.")
