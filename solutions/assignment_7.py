# Assignment 7: Write a python program which contains a dictionary with specific data. The script should accept the key name from command line and output its value from the dict. When specific key is not present in dict, it should give a specific message rather than throwing error and abruptly stopping execution and ask for next input.

myDict = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
}


def print_eng_spelling():
    flag = False

    while not flag:
        user_input = input("Enter number: ")
        try:
            print(myDict[user_input])
            flag = True
        except KeyError as e:
            print(f"Error {e} does not exist in the dictionary. Try again.")


if __name__ == "__main__":
    print_eng_spelling()
