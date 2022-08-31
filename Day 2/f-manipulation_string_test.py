# life in weeks chalange.
age = input("what is your current age? ")
years = 365
weeks = 52
months = 12
age_as_int = int(age)  # converting a string to an iteger

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12


massage = (
    f"you have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left.")
print(massage)  # f strig manipulation is done to display the output massage.
