def findNumbers(nums):
    count = 0
    for i in nums:
        i = len(str(i))
        if i % 2 == 0:
            count += 1
    return count

print(findNumbers([555,901,482,1771]))