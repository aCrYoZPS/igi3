def taylor(x: float, n: int) -> float:
    return 2/((2*n + 1) * x ** (2*n + 1))


def calculate_series(x: float, precision: float) -> int:
    """
    Function that calculates number of iterations necessary to calculate value of function ln(x+1)/ln(x-1)
    with specified precision
    :param x: this is the point at which the function is evaluated
    :param precision: this is precision with which function is evaluated
    :returns: number of iterations to reach specified precision
    :raises ArithmeticError: raises an exception when the calculation takes more than 500 iterations
    :raises ValueError: raises an exception when the argument absolute value exceeds 1
    """
    n = 1
    delta = taylor(x, 0)

    if abs(x) <= 1:
        raise ArithmeticError(f"The specified series doesn't converge for argument value of {x}")

    while delta > precision:
        delta = taylor(x, n)
        n += 1

        if n > 500:
            raise ArithmeticError(
                "The series didn't reach specified precision in 500 iterations." +
                f"It's likely it doesn't converge for argument value of {x}"
            )

    return n
