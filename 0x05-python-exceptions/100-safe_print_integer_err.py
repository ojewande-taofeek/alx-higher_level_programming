#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    # function that prints an integer.
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as vt:
        print("Exception: {}".format(vt), file=sys.stderr)
        return False
