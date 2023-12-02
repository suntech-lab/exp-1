# prompts the user
word = str(input('enter your word: '))

# if its less than five characters
if len(word) < 5:

    print(f'\'{word}\' is less than 5 characters long')

# else, if its five characters
elif len(word) == 5:

    print(f'\'{word}\' is five characters long')

# else, its more than five characters
else:

    print(f'\'{word}\' is more than five characters long')
