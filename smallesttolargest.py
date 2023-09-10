import random

def gen_list(size):
    i = 0
    list = []
    while i < size:
        list.append(random.randint(0, 10))
        i += 1
    return list

def sort_list(list):
    n = len(list)
    swapped = false
    for i in range(n-1):
        for j in range(0, n-i-1):
            if list[j] > list[j + 1]:
                swapped = true
                list[j], list[j + 1] = list[j + 1], list[j]
        if not swapped:
            return
    

    
def sorted_list(arg):
    list = gen_list(10)
    max = 0
    i = 0
    while i < len(list):
        for i in list:
            if max < list[i]:
                max = list[i]
                i += 1
            else:
                i += 1
