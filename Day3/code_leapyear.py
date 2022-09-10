# thi program checks if a year is a leap year.
# nested loop used
year = int(input("which year do you  want to check?\n"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not a leap year.")
