# ceasar cipher
# fuctions with imputs
#Arguments & parameters
# def greet():
#     print("hello erick")
#     print("i love your shirt")
#     print("have a good day")


# greet()

# def greet_with_name(name):
#     print(f"hello {name}")
#     print(f"how do you do {name}?")
#     print(f"i love your shirt {name}")


# greet_with_name("erick adikah")

# def greet_with(name, location):
#     print(f"hello {name}")
#     print(f"what is it like in {location}")


# # greet_with("erick adikah", "Nairobi")
# greet_with(location="Nairobi", name="erick adikah")

import math


def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"you'll need {num_of_cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
