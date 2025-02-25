def THEWORKS():
    n = int(input().strip())
    weather = [input().strip() for _ in range(n)]
    def SStreak(arr):
        mStreak, cStreak = 0, 0
        for day in arr:
            if day == 'S':
                cStreak += 1
                mStreak = max(mStreak, cStreak)
            else:
                cStreak = 0
        return mStreak
    mConsecutive = SStreak(weather)
    for i in range(n):
        if weather[i] == 'P':
            weather[i] = 'S'
            mConsecutive = max(mConsecutive, SStreak(weather))
            weather[i] = 'P'
    print(mConsecutive)

THEWORKS()
