def sum_of_digit_cubes(n):
    # Pre: the number that will have its digits cubed and added
    # Post: turns everything into a string and adds the cubes of the string by iterating over it
    return sum(int(digit) ** 3 for digit in str(n))

def find_special_numbers():
    # Pre: no arguement
    # Post: returns a list called special_numbers containing the numbers whos digits' cubes add up to themselves
    special_numbers = []
    for number in range(10, 10000):
        if number == sum_of_digit_cubes(number):
            special_numbers.append(number)
    return special_numbers


special_numbers = find_special_numbers()
print(special_numbers)