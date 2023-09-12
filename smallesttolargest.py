import random

def gen_list(size):
    i = 0
    list = []
    while i < size:
        list.append(random.randint(0, 100))
        i += 1
    return list

def sort_list(list):
    n = len(list)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if list[j] > list[j + 1]:
                swapped = True
                list[j], list[j + 1] = list[j + 1], list[j]
                print(list)
        if not swapped:
            return

print('sorting...')
list = gen_list(32)
sort_list(list)