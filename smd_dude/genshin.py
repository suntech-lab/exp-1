import time
import random

# pre: bubble sort
def bubblesort(list):
    swapped = False
    comparisons = 0
    for i in range(len(list) - 1):
        for j in range(0, len(list) - i - 1):
            comparisons += 1
            if list[j] > list[j + 1]:
                swapped = True
                list[j], list[j + 1] = list[j + 1], list[j]
        if not swapped:
            return list, comparisons
    return list, comparisons
# post: sorted list and comparisons made

# pre: insertion sort
def insertionsort(list):
    comparisons = 0
    for j in range(1, len(list)):
        value_to_sort = list[j]
        while list[j - 1] > value_to_sort and j > 0:
            comparisons += 1
            list[j], list[j - 1] = list[j - 1], list[j]
            j -= 1
    return list, comparisons
# post: sorted list and comparisons made

# pre: selection sort
def selectionsort(list):
    comparisons = 0
    for i in range(len(list) - 1):
        smallindex = i
        for j in range(i + 1, len(list)):
            comparisons += 1
            if list[smallindex] > list[j]:
                smallindex = j
        list[i], list[smallindex] = list[smallindex], list[i]
    return list, comparisons
# post: sorted list and comparisons made

# pre: quick sort
def quicksort(list):
    if len(list) <= 1:
        return list, 0
    pivot = list.pop()
    items_greater = []
    items_lower = []
    comparisons = 0
    for item in list:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
        comparisons += 1
    sorted_lower, comparisons_lower = quicksort(items_lower)
    sorted_greater, comparisons_greater = quicksort(items_greater)
    return sorted_lower + [pivot] + sorted_greater, comparisons + comparisons_lower + comparisons_greater
# post: sorted list and comparisons made

# pre: binary search
def binarysearch(list, target):
    left = 0
    right = 9999
    checks = 0
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return checks
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        checks += 1
    return
# post: number of checks made to find the target

# pre: generates a list
def genlist(size):
    return [random.randint(0, 10000) for _ in range(size)]
# post: a list

sorts = [
    {'sort': 'bubble', 'func': bubblesort},
    {'sort': 'quick', 'func': quicksort},
    {'sort': 'selection', 'func': selectionsort},
    {'sort': 'insertion', 'func': insertionsort},
]

# pre: gives user a prompt, uses the function that is in the same dict as the user's input, times the function, uses the binary search, prints results
def prompt(sorts):
    for op in sorts:
        print(f"type {op['sort']} for {op['sort']}sort")

    user_op_choice = input('\nput your answer here or sum shit: ')
    for op in sorts:
        if user_op_choice == str(op['sort']):

            list = genlist(10000)
            oglist = str(list[0:5]) + '...' + str(list[-6:-1])
            print(f'list before sushi: {oglist}')

            t0 = time.time()
            newlist, comparisons = op['func'](list)
            t1 = time.time()
            newlist_display = str(newlist[0:5]) + '...' + str(newlist[-6:-1])
            print(f'list after sushi: {newlist_display}')
            print(f'{t1 - t0:.2f} seconds')
            print(f'comparisons made: {comparisons}')
            target = int(input('what number are you looking for: '))
            if binarysearch(newlist, target):
                print(f'it took {binarysearch(newlist, target)} checks to find your stupid ass integer your babygirl {target}')
            else:
                print('its not here')
            break
    else:
        print('invalid input, get outta here')
# post: the answers

prompt(sorts)