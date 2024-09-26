class shape :
    def area(self):
        raise NotImplementedError("Sebclass must implement abstract method")
class Rectangle(shape):
    def __init__(self, width, height) -> None:
       self.width = width
       self.height = height

    def area(self):
        return self.width * self.height
    
class circle(shape):
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def area(self):
        import math
        return math.p1 * (self.radius **2 )

shapes = [Rectangle(10, 20), circle(5)]

for shape in shape:
    print(f"Area: {shape.area()}")