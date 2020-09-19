def maxProduct(nums):
    curr_min = curr_max = prev_max = prev_min = result = nums[0]    #assigning all variables to nums[0]

    for i in range(1, len(nums)):   #here we are starting from 1 because we already considered nums[0]
        curr_max = max(prev_max*nums[i], prev_min*nums[i], nums[i])
        curr_min = min(prev_max*nums[i], prev_min*nums[i], nums[i])
        result = max(curr_max, result)

        prev_max = curr_max
        prev_min = curr_min
    return result

print(maxProduct([2,3,-2,4]))
#print(maxProduct([0,2]))