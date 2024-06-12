class Shapes():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calcArea(self):
        print(self.base*self.height)
    
class Square(Shapes):
    def __init__(self, base, height):
        super().__init__(base, height)

class Rectangle(Shapes):
    def __init__(self, base, height):
        super().__init__(base, height)

class Trapezoid(Shapes):
    def __init__(self, base, height, base2):
        super().__init__(base, height)
        self.base2 = base2

    def calcArea(self):
        print(((self.base + self.base2)/2)*self.height)
    
class Triangle(Shapes):
    def __init__(self, base, height):
        super().__init__(base, height)

    def calcArea(self):
        print((self.base * self.height)/2)

height = int(input("height of shape?: "))
base = int(input("base of shape?: "))
base2 = int(input("second base if trapeziod?: "))

sq = Square(base, height)
rct = Rectangle(base, height)
tri = Triangle(base, height)
trp = Trapezoid(base, height, base2)

sq.calcArea()
rct.calcArea()
tri.calcArea()
trp.calcArea()