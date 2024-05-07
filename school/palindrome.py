class Solution(object):
    def isPalindrome(self, x):
        
        small_index = 0
        large_index = -1
        
        for i in range(len(x)//2):
            if x[small_index] != x[large_index]:
                return False
            small_index += 1
            large_index -= 1
        return True
            
x = input('?:')

answer = Solution().isPalindrome(str(x))
print(answer)