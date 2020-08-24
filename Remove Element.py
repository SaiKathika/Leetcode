def removeElement(nums, val):
    lst = [i for i in nums if i == val]
    for i in lst:
        for j in nums:
            if i == j:
                nums.remove(i)
    return len(nums)
print(removeElement([0,1,2,2,3,0,4,2], 2))