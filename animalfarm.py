

import time
import random

class Being():
    def __init__(self, species, sound, belly, sleep):
        self.species = species

class Lazy(Being):
    def __init__(self, species, sound, belly, sleep):
        super().__init__(species, sound, belly, sleep)
        self.sleep = sleep

    def sleeping(self):
        time.sleep(random.randint(5, 10))
        return f'{self.species} is still sleeping after {self.sleep} hours. what a lazy animal.'
    
    def description(self):
        return f'this animal is a {self.species}'

class Animal(Being):
    def __init__(self, species, sound, belly, sleep):
        super().__init__(species, sound, belly, sleep)
        self.sound = sound
        self.belly = belly

    def speak(self):
        time.sleep(random.randint(5, 10))
        return f'{self.species}: {self.sound}!'
    
    def description(self):
        return f'this animal is a {self.species}'
    
class Carnivore(Animal):

    def __init__(self, species, sound, belly, walk, sleep):
        super().__init__(species, sound, belly, sleep)
        self.walk = walk
    
    def is_hungry(self):
        time.sleep(5)
        self.belly -= 1
        if self.belly < 1:
            print(f'{self.species} would like to eat a tuna...{self.species} ate a tuna. yummy!')
            self.belly += 5
    
    def walking(self):
        time.sleep(random.randint(5, 10))
        return f'{self.species} is walking... {self.species} is now at {(self.walk[0] + random.randint(-5, 5)), (self.walk[1] + random.randint(-5, 5))}'

    
class Herbivore(Animal):
    def __init__(self, species, sound, belly, fly, sleep):
        super().__init__(species, sound, belly, sleep)
        self.fly = fly
        
    def is_hungry(self):
        self.belly -= 1
        if self.belly < 1:
            print(f'{self.species} would like to eat a seed...{self.species} ate a seed. yummy!')
            self.belly += 5

    def flying(self):
        time.sleep(random.randint(5, 10))
        return f'{self.species} is flying... {self.species} is now at {(self.fly[0] + random.randint(-5, 5)), (self.fly[1] + random.randint(-5, 5))}'

class Panda(Animal, Lazy):#multiple inheritance, it took a really long time because i had to figure out how super worked
    def __init__(self, species, sound, belly, sleep):
        super().__init__(species, sound, belly, sleep)

    def is_hungry(self):
        self.belly -= 1
        if self.belly < 1:
            print(f'{self.species} would like to eat bamboo...{self.species} ate a bamboo. yummy!')
            self.belly += 5


def panda():
    choice = random.randint(0,3)
    if choice == 0:
        print(mrsleep.speak())
    elif choice == 1:
        print(mrsleep.sleeping())
    elif choice == 2:
        mrsleep.is_hungry()
    

def parrot():
    choice = random.randint(0,3)
    if choice == 0:
        print(parry.speak())
    elif choice == 1:
        print(parry.flying())
    elif choice == 2:
        parry.is_hungry()

def kitty():
    choice = random.randint(0,3)
    if choice == 0:
        print(tabby.speak())
    elif choice == 1:
        print(tabby.walking())
    elif choice == 2:
        tabby.is_hungry()


mrsleep = Panda('Panda', 'roar', 0, 10)
tabby = Carnivore('Tabby cat', 'meow', 0, (0, 0), None)
parry = Herbivore('Cockatoo', 'chirp chirp', 0, (0, 0), None)
print(parry.description())
print(tabby.description())
print(mrsleep.description())

while True:
    kitty()
    parrot()
    panda()
