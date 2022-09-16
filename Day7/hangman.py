# for loop
# hangman project.
# Step 1

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_lenth = len(chosen_word)

print(f'psst, the chosen solution is {chosen_word}.')

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
display = []
for _ in range(word_length):
    display += "-"

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for position in range(word_lenth):
    letter = chosen_word[position]
    print(
        f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
        display[position] = letter
print(display)
# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
display = []
word_lenth = (len(chosen_word))
for _ in range(word_lenth):
    display += "-"
# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
for position in range(word_lenth):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)
