from my_io.menu import menu_item


@menu_item(3)
def analyze_text(text: str):
    res = 0
    for ch in text:
        if ch.isnumeric() or (ch.isalpha() and ch.isupper()):
            res += 1

    return res
