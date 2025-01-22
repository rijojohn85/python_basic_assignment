# Assignment 6: Write a program which will be able to accept Student data with help of different functions, to eventually store all data in one dictionary, and finally print out all content of that dictionary variable.


def student(**kwargs) -> dict:
    my_dict = {}
    for key, value in kwargs.items():
        my_dict[key] = value
    return my_dict


print(student(name="rijo", id=1, grade=10, average_marks=85))
