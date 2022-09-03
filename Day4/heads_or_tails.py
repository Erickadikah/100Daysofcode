import random

random_side = random.randint(0, 1)  # picks randomly
if random_side == 1:
    print("Heads")
elif random_side == 0:
    print("Tails")
