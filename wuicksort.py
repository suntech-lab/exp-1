import random
import timeit

def gen_list(size):
    i = 0
    list = []
    while i < size:
        list.append(random.randint(0, 1000))
        i += 1
    return list

def quick_sort(list):
    length = len(list)
    if length <= 1:
        return list
    else: 
        pivot = list.pop()

    items_greater = []
    items_lower = []

    for item in list:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


list = gen_list(10)
print(list)
print('sorting...')
print(quick_sort(list))
print(f' it took {timeit.default_timer()} nanoseconds to sort')
