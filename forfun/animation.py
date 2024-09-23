import time
pattern = ['#','#','#','#','.','.','.','.','.','.']

while True:
    pattern = ' '.join(pattern)
    print(pattern)
    time.sleep(0.1)
    pattern = pattern.split(' ')
    pattern = pattern[1:10]
    pattern.append(pattern[0])

