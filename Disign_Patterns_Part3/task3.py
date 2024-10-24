import copy
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def draw(self):
        pass

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Shape Type: {self.shape_type}"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def draw(self):
        print(f"Drawing a Circle with radius {self.radius}")

    def __str__(self):
        return f"Shape Type: {self.shape_type}, Radius: {self.radius}"


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing a Rectangle with width {self.width} and height {self.height}")

    def __str__(self):
        return f"Shape Type: {self.shape_type}, Width: {self.width}, Height: {self.height}"


if __name__ == "__main__":
    original_circle = Circle(5)
    original_rectangle = Rectangle(4, 6)

    print("Original Shapes:")
    print(original_circle)
    original_circle.draw()

    print(original_rectangle)
    original_rectangle.draw()

    cloned_circle = original_circle.clone()
    cloned_rectangle = original_rectangle.clone()

    cloned_circle.radius = 10
    cloned_rectangle.width = 8
    cloned_rectangle.height = 12

    print("\nCloned and Modified Shapes:")
    print(cloned_circle)
    cloned_circle.draw()

    print(cloned_rectangle)
    cloned_rectangle.draw()

    print("\nOriginal Shapes After Cloning:")
    print(original_circle)
    print(original_rectangle)
