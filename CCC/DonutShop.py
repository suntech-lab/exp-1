openDonutsAvailable = int(input())
events = int(input())

def donutshop(openDonutsAvailable, events):
    bakeOrSell = input()
    if bakeOrSell == '+':
        baked = int(input())
        openDonutsAvailable += baked
        events -= 1
        if events == 0:
            print(openDonutsAvailable)
            exit()
        donutshop(openDonutsAvailable, events)
    else:
        sold = int(input())
        openDonutsAvailable -= sold
        events -= 1
        if events == 0:
            print(openDonutsAvailable)
            exit()
        donutshop(openDonutsAvailable, events)

donutshop(openDonutsAvailable, events)


