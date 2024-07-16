import math

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def get_perimeter(self):
        # The perimeter is also known as the circumference for a circle
        return 2 * math.pi * self.radius

    def get_circumference(self):
        return self.get_perimeter()

# Example of creating a Circle object and performing operations
circle = Circle(0, 0, 24)

# Calculating area
print(f"Area of the circle: {circle.get_area()}")

# Calculating perimeter
print(f"Perimeter of the circle: {circle.get_perimeter()}")

# Calculating circumference
print(f"Circumference of the circle: {circle.get_circumference()}")
