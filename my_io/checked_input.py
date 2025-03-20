def input_int() -> int:
    """
    Function that takes user input and checks it
    :returns: correct whole number
    """
    while True:
        input_str = input("Input a number")
        if float(input_str) != int(input_str):
            print("Invalid input. Input input_str whole number: ")
        else:
            return int(input_str)
