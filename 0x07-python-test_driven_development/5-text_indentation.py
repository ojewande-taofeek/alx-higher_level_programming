#!/usr/bin/python3
""" Contains a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
        function that prints a text with 2 new lines after
        each of these characters: ., ? and :
        Args:
            text(str): string to be updated
        Returns:
            Nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    pun = None
    for word in text:
        if word == "." or word == "?" or word == ":":
            pun = word
            print("{}\n".format(word))
        elif pun and word == " ":
            pun = None
            continue
        else:
            print(word, end="")
