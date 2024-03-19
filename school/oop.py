# dog.py

class Bird:

    def __init__(self, name, age, colour, species):
        self.name = name
        self.age = age
        self.colour = colour
        self.species = species


    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old and is {self.colour} from the {self.species} species."
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
class Human:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def description(self):
        return f"i am {self.age} years old and my name is {self.name} and i am in grade {self.grade}"
    
    def speak(self, word):
        return f'{self.name} says {word}'

# super() = Function used to give access to the methods of a parent class.
#                  Returns a temporary object of a parent class when used

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, length, width):

        super().__init__(length,width)

    def area(self):
        return self.length*self.width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length,width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height
    
class Triangle():

    def __init__(self, height, base):
        self.height = height
        self.base = base

class Right(Triangle):
    def __init__(self, height, base):
        super().__init__(height, base)

    def area(self):
        return (self.height*self.base)/2

class Animal:
  def __init__(self, Animal):
    print(Animal, 'is an animal.');

class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    super().__init__(mammalName)
    
class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammal):
    print(NonWingedMammal, "can't fly.")
    super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammal):
    print(NonMarineMammal, "can't swim.")
    super().__init__(NonMarineMammal)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.');
    super().__init__('Dog')
    
d = Dog()
print('')
bat = NonMarineMammal('Bat')
    
sl = int(input('length of square:'))
sw = int(input('width of square:'))
cl = int(input('length of cube:'))
cw = int(input('width of cube:'))
ch = int(input('height of cube:'))
th = int(input('height of triangle:'))
tb = int(input('base of triangle:'))

triangle = Right(th, tb)
square = Square(sl, sw)
cube = Cube(cl, cw, ch)

print(f' the area of the square is {square.area()}.')
print(f'the volume of the cube is {cube.volume()}.')
print(f'the area of the right triangle is {triangle.area()}')

eric = Human('Eric', 14, 10)

woodstock = Bird('woodstock', 57, 'yellow', 'birdus smallus')

bigbird = Bird('big bird', 6, 'yellow', 'birdus biggus')

print(bigbird.description())
print(woodstock.description())
print(eric.description())

print(bigbird.speak('super dooper flooper hooper hooper hooper!!!'))
print(woodstock.speak('1l1l1l11ll1lll11l1ll11l1l1l1l1l1l1l11ll1l1l11l1l111l1l1l1l1l'))
print(eric.speak('pizza'))