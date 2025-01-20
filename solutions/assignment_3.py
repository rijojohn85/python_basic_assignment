# Assignment 3: Traversing through below list of digits, filter out the numbers which are divisible by 5.

# list = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
#
def filter_list():
    list = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
    div_5 = [num for num in list if num % 5 == 0]
    return div_5


if __name__ == "__main__":
    print(filter_list())
