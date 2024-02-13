class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def Area(self):
        return self.length * self.width
    
    def Perimeter(self):
        return (self.length + self.width) * 2
    
r1 = Rectangle(12, 10)
print(r1.Perimeter())
print(r1.Area())