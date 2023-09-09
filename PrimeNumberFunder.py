n = 0
while n < 100000:
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print(n)
    n += 1
