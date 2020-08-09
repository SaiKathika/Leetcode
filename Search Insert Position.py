def searchInsert(nums, target):
    start = 0
    end = len(nums)
    while start < end:
        mid = (start + end)//2
        if nums[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return start