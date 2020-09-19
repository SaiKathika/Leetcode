#dynamic programming
def rob(nums):
    a, b = 0, 0
    # [a, b, i, i+1, ...]
    for i in nums:
        #print('a', a)
        #print('b', b)
        #print('i', i)

        a, b = b, max(a + i, b)
        #print('after a', a)
        #print('after b', b)
    return b

print(rob([2,1,1,2]))