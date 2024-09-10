import time
pattern = ['#','#','#','.','.','.','.','.','.']

while True:
    pattern = ' '.join(pattern)
    print(pattern)
    time.sleep(0.1)
    pattern = pattern.split(' ')
    pattern = pattern[1:9]
    pattern.append(pattern[0])

