import random

word_list = ["baboo", "elephant", "monkey", "lamar", "camel"]
# using random for the choice to be randon.
chosen_word = random.choice(word_list)

print(f"the chosen solution is {chosen_word}")
# this prints randomly chosen word and assign it to a variable called chosen_word.
display = []
for _ in range(word_lenth):
    display += "-"
# asking the user to guess a letter and assign their answer to a variable called guess. in lower case
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_lenth):
        letter = chosen_word[position]
        print(
            f"Currentposition: {position}\n Curren letter: {letter}\n Gussed letter: {guess}")
    print(display)
# check if the letter guessed by the user is one of the  chosen_word.
# loop through each position in the chosen_word.
# if letter at position matches "guess" raeveal letter in the diplayat position.

# prin "display" and you should see the guessed letter in the correct position
# and any other repl NB dont worry about getting the user to guess the next letter
if "-" not in display:
    end_of_game = True
    print("You win")

# for position in range(word_lenth):
#     letter = chosen_word[position]
#     if letter == guess:
#         display[position] = letter


print(display)
