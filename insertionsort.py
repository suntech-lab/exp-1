import random
import timeit

def gen_list(size):
    i = 0
    list = []
    while i < size:
        list.append(random.randint(0, 1000))
        i += 1
    return list


def insertion_sort(list):
    indexing_length = range(1, len(list))
    for j in indexing_length:
        value_to_sort = list[j]

        while list[j - 1] > value_to_sort and j > 0:
            list[j], list[j - 1] = list[j - 1], list[j]
            j -= j

    return list

list = gen_list(10)
print(list)
print('sorting...')
print(insertion_sort(list))
print(f' it took {timeit.default_timer()} nanoseconds to sort')