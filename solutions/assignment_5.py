# Assignment 5: Write a program in Python which will be able to accept any number of arguments in the same function and can process it.


def average(*args):
    return sum(args) / len(args)


if __name__ == "__main__":
    assert average(1, 2, 3, 4, 5) == 3.0
