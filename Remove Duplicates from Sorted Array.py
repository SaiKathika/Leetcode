'''
def removeDuplicates(nums):
    a = list(dict.fromkeys(nums))
    nums[:] = a
    print(nums)
    return len(nums)

print(removeDuplicates([-1,0,0,0,0,3,3]))
'''

#Inplace ->

def removeDuplicates(nums):
    if len(nums) == 0: return 0
    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

print(removeDuplicates([-1,0,0,0,0,3,3]))