height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

weight_as_int = int(weight)
height_as_float = float(height)


# using the exponet operator **
#bmi = int(weight) / float(height) ** 3
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi_as_int = int(bmi)

print(bmi_as_int)
