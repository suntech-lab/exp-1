import random
import timeit

def gen_list(size):
    i = 0
    list = []
    while i < size:
        list.append(random.randint(0, 1000))
        i += 1
    return list

def bubble_sort(list):
    length = len(list)
    swapped = False
    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if list[j] > list[j + 1]:
                swapped = True
                list[j], list[j + 1] = list[j + 1], list[j]
        if not swapped:
            return

list = gen_list(100)
print(list)
print('sorting...')
bubble_sort(list)
print(list)
print(f' it took {timeit.default_timer()} nanoseconds to sort')