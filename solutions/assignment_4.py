# Assignment 4: Write a python program which keeps reading content from command line until the content is 'quit', and then writes the content before quit to a file.
def write_to_file():
    user_input = ""
    output = ""
    while user_input != "quit":
        output += user_input
        user_input = input("enter text: ")

    with open("output.txt", "w") as file:
        file.write(output)


if __name__ == "__main__":
    write_to_file()
