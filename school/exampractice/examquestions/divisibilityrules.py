x = int(input('what is your number: '))

def SnapCrackle(x):
    if x%3 == 0:
        if x%5 == 0:
            print('SnapCrackle')
            return
    if x%3 == 0:
        print("Crackle")
        return
    if x%5 == 0:
        print("Snap")
        return

SnapCrackle(x)