# maze direct the robot.
# the robot goes to any direaction
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if rigth_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
# come back debug.
