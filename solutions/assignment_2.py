# Assignment 2: Write a python program to print out the Fibonacci series of digits between 1 to 100. Try to achieve this using all the types of loop available in python.
#


def fibonacci_whileloop():
    print("With while loops")
    i, prev = 1, 0
    while i < 100:
        print(i)
        prev, i = i, i + prev


def fibonacci_forloop():
    print("With for loops")
    i, prev = 1, 0
    for _ in range(100):
        print(i)
        prev, i = i, i + prev
        if i > 100:
            break

def rec_fibonacci(n):
    if n <= 1:
        return n
    return rec_fibonacci(n-1) + rec_fibonacci(n-2)




if __name__ == "__main__":
    print("With while loop:")
    fibonacci_whileloop()
    print("With for loop:")
    fibonacci_forloop()
    print("With recursion")
    for i in range(100):
        fib = rec_fibonacci(i)
        if fib > 100:
            break
        print(fib)
