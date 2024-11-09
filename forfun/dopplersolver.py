sosound = 346
sosource = input('speed of source in meters/second: ')
fosource = input('frequency of sound from source in Hz: ')

def towards():
    global direction
    direction = 'towards'

def away():
    global direction
    direction = 'away'

directionschema = [
    {'direction': '0', 'description': 'towards', 'func': towards},
    {'direction': '1', 'description': 'away', 'func': away}]

def sourcedirectiondecision():
    for op in directionschema:
        print(f"enter {op['direction']} to set the source as {op['description']}")

    choice = input('\nenter here: ')

    for op in directionschema:
        if choice == str(op['direction']):
            op['func']()
            break
        else:
            print('invalid input, please put in a valid input.')
            exit()

sourcedirectiondecision()

def solve():
    if direction == 'towards':
        foobserver = (sosound/(sosound - sosource))*fosource
    if direction == 'away':
        foobserver = (sosound/(sosound + sosource))*fosource

    print(foobserver)

solve()