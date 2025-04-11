import random
import time

listvictim = []

for i in range(10):
    listvictim.append(random.randint(1, 10))

sleeptimes = {}

for i in listvictim:
    sleeptimes[i] = i


