from concurrent.futures import ProcessPoolExecutor
from platform import python_version_tuple


print("Welcome to the tip calculator!")
bill = float(input("what is the total bill $"))
tip = int(input("how much would you like to give? 10, 12, or 15? "))
people = int(input("how many people to split the bill?"))
tip_as_percent = tip / 100
total_bill = bill * tip_as_percent
total_bill = bill * tip_as_percent
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)
print(f"each person should pay: ${final_amount}")
