# love  meter calculator
print("Welcome to the love Calculator")
name1 = input("what is your name?\n")
name2 = input("what is their name?\n")

combine_string = name1 + name2  # combining two strings

# changing the string to lower case in case input was in upper case.
lower_case_string = combine_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
# counting the latters true in the combine string.
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e  # adding  how many no. th latters occur in the strings

l = lower_case_string.count("l")
o = lower_case_string.count("o")  # counting the latters love in the string
v = lower_case_string.count("v")
e = lower_case_string.count("e")

# adding the values and deternining how many times the values where passed.
love = l + o + v + e

# converting a string to an interger. and adding the values.
love_score = int(str(true) + str(love))


print(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"your score is {love_score} you go together like coke and menthol")
elif (love_score >= 40) and (love_score <= 50):
    print(f"your love score is {love_score} you are alright together.")
else:
    print(f"your love score is {love_score}")
