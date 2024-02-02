# dog.py

class Bird:
    species = "Birdis Biggus"

    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old and is {self.colour}"
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

woodstock = Bird('woodstock', 57, 'yellow')

bigbird = Bird('big bird', 6, "yellow")

print(bigbird.description())
print(woodstock.description())

print(bigbird.speak('super dooper flooper hooper hooper hooper!!!'))
print(woodstock.speak('1l1l1l11ll1lll11l1ll11l1l1l1l1l1l1l11ll1l1l11l1l111l1l1l1l1l'))