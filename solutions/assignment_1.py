# Assignment 1: Write a python script which will be able to accept the data on command line as input and will be able to identify and print out the datatype of the given input.
#
import re
import sys


def check_input_type():
    if len(sys.argv) < 2:
        print("Please provide input")
        return
    input_from_user = sys.argv[1]
    # regex for float:
    # ^-? - starts with '-' with either 0 or 1 char: ie could be -1.1 or 1.1 ? - means count of 0 or 1
    # \d+ - digits - 1 or more - \ to escape d - digit + - 1 or more
    # \. - 1 '.'
    # \d+$ - 1 or more digits and ends with it.

    float_pattern = r"^-?\d+\.\d+$"

    if input_from_user.isdigit():
        print(f"Input: {input_from_user} is of type int")
    elif re.match(float_pattern, input_from_user):
        print(f"Input: {input_from_user} is of type float")
    elif input_from_user.lower() in ["true", "false"]:
        print(f"Input: {input_from_user} is of type Boolean")
    else:
        print(f"Input: {input_from_user} is of type String")


if __name__ == "__main__":
    check_input_type()
