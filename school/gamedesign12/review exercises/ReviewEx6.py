"""
Review Exercise 6 GameDesign 12
Eric Liu
23/02/2025
"""

import re
from collections import deque

def reverse(sIterable):
        oDeque = deque()
        oDeque.extendleft(sIterable)
        return ''.join(oDeque)

def isPalindrome(sVictim):
    
    sVictim = sVictim.replace(' ', '')
    sVictim = re.sub(r'[^a-zA-Z0-9]', '', sVictim)
    sVictim = sVictim.lower()

    iSmallIndex = 0
    iLargeindex = -1
    
    for i in range(len(sVictim)//2):
        if sVictim[iSmallIndex] != sVictim[iLargeindex]:
            return False
        iSmallIndex += 1
        iLargeindex -= 1
    return True

def isPalindromeNoLoop(sVictim):
    
    sVictim = sVictim.replace(' ', '')
    sVictim = re.sub(r'[^a-zA-Z0-9]', '', sVictim)
    sVictim = sVictim.lower()

    if reverse(sVictim) == sVictim:
        return True
    return False
  
sVictim = input('?:')

bAnswer = isPalindromeNoLoop(sVictim)
print(bAnswer)