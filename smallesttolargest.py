import random
import time

def gen_list(size):
    i = 0
    list = []
    while i < size:
        list.append(random.randint(0, 100))
        i += 1
    return list

def sort_list(list):
    length = len(list)
    swapped = False
    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if list[j] > list[j + 1]:
                swapped = True
                list[j], list[j + 1] = list[j + 1], list[j]
                print(list)
                time.sleep(0.01)
        if not swapped:
            return

print('sorting...')
list = gen_list(35)
sort_list(list)