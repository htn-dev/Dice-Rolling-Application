# dice.py

def parse_input(input_string):
    """Return `input_string` as an integer between 1 and 6.


    Check if `input_string` is an integer number between 1 and 6.

    If so, return an integer with the same value. Otherwise, tell

    the user to enter a valid number and quit the program.

    """
    if input_string.strip() in {"1","2","3","4","5","6"}:
        return int(input_string)
    


# ~~~ App's main code block ~~~
# 1. Get and Validate user's input
num_dice_input = input("How many dice do you want to roll? [1-6] ")
num_dice = parse_input(num_dice_input)


