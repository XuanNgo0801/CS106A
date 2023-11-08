from karel.stanfordkarel import *

def main():
    while front_is_clear():
        create_row()
        move_to_next_row()
    create_row()  # Create the last row

# Function to create a row of the checkerboard
def create_row():
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()

# Function to move Karel to the next row
def move_to_next_row():
    if facing_east():
        turn_left()
        if front_is_clear():
            move()
            turn_left()
    else:
        turn_right()
        if front_is_clear():
            move()
            turn_right()

# Turn Karel right
def turn_right():
    for i in range(3):
        turn_left()

# Turn Karel around
def turn_around():
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program()