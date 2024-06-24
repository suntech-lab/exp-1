import random

def get_max(arg):
    max = 0
    for i in list:
        if i > max:
            max = i
    print(f"Max is {max}")

def sort(arg):
    print("sort function")

def gen_list(size):
    i = 0
    list = []
    while i < size:
        list.append(random.randint(1, 100))
        i += 1
    return list

list = gen_list(20)
print(f"Generate list {list}")
get_max(list)
