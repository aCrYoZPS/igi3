from menu.menu import menu_item
from my_io import checked_input


@menu_item(5)
def calculate_floats():
    """
    Function prompts user to input a sequence of floating point numbers and
    finds the number with lowest absolute value and sum of all number after
    the first positive one
    :returns: tuple of format (min_abs_index, min_abs, sum)
    """
    n = checked_input.input_int()
    min_abs = -1
    min_abs_index = 0
    counter = 0
    sum = 0
    positive_encountered = False

    for number in checked_input.gen_floats(n):
        if abs(number) < min_abs:
            min_abs_index = counter
            min_abs = abs(number)

        if positive_encountered:
            sum += number

        if number > 0:
            positive_encountered = True

        counter += 1

    return (min_abs_index, min_abs, sum)
