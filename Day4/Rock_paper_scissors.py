import random
# this a rock papers and sciscoors game.

game_images = ['rock', 'paper', 'scissors']

user_choice = int(input(
    "what do you choose? type 0 for rock, 1 for paper or  2 for scissors.\n"))
print(game_images[user_choice])
# asks user to choose an in put.

# this function make scomputer choose randomly between 0-2 numbres.
computer_choice = random.randint(0, 2)
print(f"computer chose {computer_choice}")


if user_choice >= 3 or user_choice < 0:
    print("invalid choice you loose.")
if user_choice == 0 and computer_choice == 2:
    print("you win!")
elif computer_choice == 0 and user_choice == 1:
    print("you lose")
elif computer_choice > user_choice:
    print("you lose")
elif user_choice > computer_choice:
    print("you win!")
elif computer_choice == user_choice:
    print("its a draw")
