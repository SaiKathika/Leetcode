#Best Solution
for l in t:
    if t.count(l) > s.count(l): return l
'''
#using Counter
from collections import Counter
def findTheDifference(s, t):
    return list((Counter(t) - Counter(s)).keys())[0]

print(findTheDifference('abcd', 'abcde'))
'''
#without Counter
def findTheDifference(s, t):
    s, t = sorted(s), sorted(t)
    for i in range(len(s)):
        if s[i] != t[i]:
            return t[i]
           
    return t[-1]

print(findTheDifference('abcd', 'abcde'))