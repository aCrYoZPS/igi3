from menu.menu import menu_item


@menu_item(4)
def analyze_text():
    """
    Function that analyzes the given text
    :returns: tuple of format (number_of_words, longest_index, longest)
    """
    text = "So she was considering in her own mind, as well as she could,"
    + "for the hot day made her feel very sleepy and stupid,"
    + " whether the pleasure of making a daisy-chain would be worth the"
    + " trouble of getting up and picking the daisies, when suddenly"
    + "a White Rabbit with pink eyes ran close by her."

    words = "".join(text.strip(".").split(",")).split(" ")

    number_of_words = len(words)

    longest_index = 0
    max_len = 0
    i = 0

    for word in words:
        if len(word) > max_len:
            max_len = len(word)
            longest_index = i

        if i % 2 == 0:
            print(word)

        i += 1

    return (number_of_words, longest_index, words[longest_index])
