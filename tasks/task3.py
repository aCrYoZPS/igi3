from my_io.menu import menu_item


@menu_item(3)
def analyze_text(text: str):
    """
    Function that calculates number of numeric symbols and uppercase letters in input string
    :param text: string to be analyzed
    :returns: number of numeric symbols and uppercase letters
    """
    res = 0
    for ch in text:
        if ch.isnumeric() or (ch.isalpha() and ch.isupper()):
            res += 1

    return res
