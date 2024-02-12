import random
import string

s = ''.join(random.choice(string.ascii_lowercase) for i in range(5))


class Solution(object):

    def __init__(self, s):
        self.s = s

    def frequencySort(self):
        list = [s[0], s[len(s -)]]
        length = len(s)
        for i in range(length - 1):
            for j in range(0, length - i - 1):
                if s[j] != s[j + 1]:
                    print(list)
                    list.append(s[j])
                    
                
        return s
    
print(Solution.frequencySort(s))

print(s[3] == s[3])
