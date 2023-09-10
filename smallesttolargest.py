import random

def gen_list(size):
    i = 0
    list = []
    while i < size:
        list.append(random.randint(0, 10))
        i += 1
    return list

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
