from abc import ABC, abstractclassmethod
from random import choice


class Shape(ABC):
    @abstractclassmethod
    def draw(self):
        """Draws a figure"""


class Rectangle(Shape):
    """Change me"""

    def draw(self):
        for i in range(1, 4):
            if i == 1 or i == 3:
                print("----")
            else:
                print("|  |")


class Circle(Shape):
    """Change me"""

    def draw(self):
        for i in range(1, 4):
            if i == 1 or i == 3:
                print(" --")
            else:
                print("-  -")


def get_shape() -> Shape:
    """
    This function should return any instance of a Shape class
    In our example it is Rectangle or Circle
    """
    options: list[Shape] = [Rectangle(), Circle()]
    return choice(options)


def main():
    """
    In Rectangle is used I'd like to see:

    ----
    |  |
    ----

    If Circle is used:
      --
     -  -
      --
    """
    shape: Shape = get_shape()
    shape.draw()


if __name__ == "__main__":
    main()
