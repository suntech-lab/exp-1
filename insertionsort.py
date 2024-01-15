import random
import time

def gen_list(size):
    i = 0
    list = []
    while i < size:
        list.append(random.randint(0, 10000))
        i += 1
    return list


def insertion_sort(list):
    indexing_length = range(1, len(list))
    for j in indexing_length:
        value_to_sort = list[j]

        while list[j - 1] > value_to_sort and j > 0:
            list[j], list[j - 1] = list[j - 1], list[j]
            j -= 1

    return list

list = gen_list(10000)
print(list)
print('sorting...')
t0 = time.time()
print(insertion_sort(list))
t1 = time.time()
print(f'{t1 - t0:.22f}')
