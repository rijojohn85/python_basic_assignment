# Assignment 8: Perform the same task as in assignment 5, but with the help of class and its object.


class Average:
    def __init__(self, *args) -> None:
        self.data = args

    def average(self) -> float:
        return sum(self.data) / len(self.data)


avg = Average(1, 2, 3, 4, 5)
print(avg.average())
assert avg.average() == 3.0
