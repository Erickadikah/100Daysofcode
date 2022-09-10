# concept of the day randomisation.
import random


random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
# this example print diffrent values everytime.
print(f"your love score is {love_score}")
