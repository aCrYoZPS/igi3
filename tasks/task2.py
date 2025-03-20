import my_io.checked_input as ci


def multiplicator():
    """
    Function that multiplies all numbers from stdin while they are less than 0
    :returns: result of multiplication
    """
    result = 1
    while True:
        a = ci.input_int()

        if a > 0:
            break

        result *= a

    return result
