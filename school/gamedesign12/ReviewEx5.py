"""
Review Exercise 5 GameDesign 12
Eric Liu
21/02/2025
"""

sOgString = 'the quick brown fox jumped over the lazy dog'
sTarget = input('what do you want to replace?: ')
sReplacement = input('what do you want to replace it with?: ')

sNewString = sOgString.replace(sTarget, sReplacement)

print(sNewString)

