#!/usr/bin/python3
def multiple_returns(sentence):
    """ function that returns a tuple with the
        length of a string and its first character
    """
    count = 0
    first = None
    if sentence:
        for char in sentence:
            count = count + 1
        first = sentence[0]
    return (count, first)
