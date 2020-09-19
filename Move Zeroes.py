def moveZeroes(nums):
    for i in nums:
        if i == 0:
            nums.remove(0)
            nums.append(0)
    return nums

print(moveZeroes([0,0,1]))