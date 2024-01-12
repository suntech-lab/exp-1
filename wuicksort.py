import random
import time

def gen_list(size):
    i = 0
    list = []
    while i < size:
        list.append(random.randint(0, 10000))
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



list = gen_list(10000)
print(list)
print('sorting...')
t0 = time.time()
print(quick_sort(list))
t1 = time.time()
print(f'{t1 - t0:.22f}')
