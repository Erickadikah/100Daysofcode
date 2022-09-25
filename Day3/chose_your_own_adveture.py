print("Welcome to Treasure Island.")
print("Your mission is to find the treasue.")
choice1 = input(
    'You\'re at a cross road. where do you want to go? Type "left" or "right" \n').lower()
if choice1 == 'right':
    print("game over you fell on a hole")
elif choice1 == 'left':
    choice2 = input(
        "you\'ve come to a lake. theres is an island in the middle of the lake. type 'wait' to wait for the boat. and 'swim' to swim accross. \n").lower()
    if choice2 == 'swim':
        print("Game over you drown and eaten by crocodiles!!.")
    else:
        choice3 = input(
            " you have arrived at the island safe there is a house with 3 doors.'yellow', 'blue', 'red' whch door do you choose\n").lower()
        if choice3 == 'yellow':
            print("you found the treasure you win hurray !!")
            if choice3 == 'blue':
                print(" you entered a room full of lions game over")
            elif choice3 == 'red':
                print("room full of fire game over!!.")
