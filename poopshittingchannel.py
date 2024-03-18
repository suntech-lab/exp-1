def cursedtechniquereversal(arg):
    red = ''
    i = 1
    while i <= len(arg):
        red += arg[-i]
        i += 1

    print(f'print(Reverse("{arg}"))\n\nwould print {red}')

cursedtechniquereversal('i am gojo satoru, and this is my story')