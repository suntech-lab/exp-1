n = 3
while n < 100000:
    x = 2
    while x < n:
        if n % x == 0:
            break
        x += 1
    else:
        print(n)
    n += 1
