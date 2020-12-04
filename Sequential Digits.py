def sequentialDigits(low, high):
    s = '123456789'
    res = []
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            a = int(s[i:j+1])   #here we are adding 1 to j bcoz in the ques they told that 10 <= low
            if low <= a <= high:
                res.append(a)            
    return sorted(res)

print(sequentialDigits(100, 300))
'''
#using queue
from collections import deque
def sequentialDigits(low, high):
    queue = deque(range(1, 10))
    lst = []
    while queue:
        e = queue.popleft()
        if low <= e <= high:
            lst.append(e)
        last = e % 10
        if last < 9: queue.append(e * 10 + last + 1)    #here we are doing this to get immediate next number
    return lst
print(sequentialDigits(100, 300))
'''