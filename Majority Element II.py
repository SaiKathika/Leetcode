'''
def majorityElement(nums):
    n = len(nums)/3
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    lst = []
    for i, j in dict.items():
        if j > n:
            lst.append(i)
    return lst

print(majorityElement([1,1,1,3,3,2,2,2]))
'''
#using Counters
from collections import Counter
def majorityElement(nums):
    a = Counter(nums)
    return [i for i, j in a.items() if j > len(nums)//3]

print(majorityElement([1,1,1,3,3,2,2,2]))