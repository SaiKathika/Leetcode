#refer the below link
#https://leetcode.com/problems/contains-duplicate-iii/discuss/824603/Python-SortedList-O(n-log-k)-solution-explained
# O(n logk)
'''
import bisect
from sortedcontainers import SortedList
def containsNearbyAlmostDuplicate(nums, k, t):
    if len(nums) == 0 or k < 0 or t < 0: return False
    s = SortedList()
    for i, n in enumerate(nums):
        if i > k: s.remove(nums[i-k-1])
        pos1 = bisect.bisect_left(s, n-t)
        pos2 = bisect.bisect_right(s, n+t)
        if pos1 != pos2: return True
        s.add(n)
    return False
    
print(containsNearbyAlmostDuplicate([1,0,1,1], 1, 2))
'''

# O(n^2)
def containsNearbyAlmostDuplicate(nums, k, t):
    if len(nums) == 0 or k < 0 or t < 0: return False
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                pass
            elif abs(nums[j]-nums[i]) <= t and abs(j-i) <= k:
                return True
    return False
print(containsNearbyAlmostDuplicate([1,0,1,1], 1, 2))