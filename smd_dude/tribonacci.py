class Solution(object):
    def __init__(self, n=0):
        self.n = n

    def tribonacci(self, n=None):
        if n == None:
            n = self.n
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

prompt = int(input('n: '))
solution = Solution(prompt)
print(solution.tribonacci())
