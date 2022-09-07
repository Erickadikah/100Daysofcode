
# for loop with range
#  total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)
total = 0
for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        # divisible by both 5 and  3
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    # divisible by 3.
    elif number % 5 == 0:
        print("buzz")
    # divisible by 5.
    else:
        print(number)
