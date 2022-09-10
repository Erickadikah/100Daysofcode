import random
# lists are data structures.
names_string = input("Give me everybody's names, separated by a comma.\n")

names = names_string.split(",")

# # gets the total number of items in list.
# num_items = len(names)
# #random.randint(0, x)

# random_choice = random.randint(0, num_items - 1)

# person_to_pay = names[random_choice]
# allows to print the name in random and with code efficiency.
person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is the person goin to pay for the meal today.")
