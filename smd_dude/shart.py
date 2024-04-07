leaderboard = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]

new_score = int(input('Enter your new score: '))

def sort(new_score):
    i = 0
    if new_score < leaderboard[-1]:
        print(leaderboard)
        exit()
    while new_score < leaderboard[i]:
        i += 1
    leaderboard.insert(i, new_score)
    leaderboard.pop()
    print(leaderboard)

sort(new_score)