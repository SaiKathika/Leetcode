def removeDuplicates(nums):
    a = list(dict.fromkeys(nums))
    nums[:] = a
    print(nums)
    return len(nums)

print(removeDuplicates([-1,0,0,0,0,3,3]))