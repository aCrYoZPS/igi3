import my_io.checked_input as ci


def multiplicator():
    """
    Function that multiplies all numbers from stdin while they are less than 0
    :returns: result of multiplication
    """
    result = 1
    numbers = ci.input_int_arr(lambda x: x < 0)

    for number in numbers:
        result *= number

    return result
