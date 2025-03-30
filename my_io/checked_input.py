def input_int() -> int:
    """
    Function that takes user input and checks it
    :returns: correct whole number
    """
    while True:
        input_str = input("Input a number")
        res = 0
        try:
            res = int(input_str)
            break
        except ValueError:
            print("Invalid input. Input whole number: ")

    return res


def input_float() -> float:
    """
    Function that takes user input and checks it
    :returns: correct floating point number
    """
    while True:
        input_str = input("Input a number")
        res = 0.0
        try:
            res = float(input_str)
            break
        except ValueError:
            print("Invalid input. Input correct real number: ")

    return res


def input_float_arr(delim: float):
    result = []
    while True:
        elem = input_float()

        if elem == delim:
            return result

        result.append(elem)
