#!/usr/bin/python3
"""
    finds peak of the a list of integers
"""
def find_peak(list_of_integers):
    """
        finds a peak in a list of unsorted integers
    """
    try:
        if isinstance(list_of_integers, list):
            return sorted(list_of_integers)[-1]
    except IndexError:
        return
