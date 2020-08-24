def findMaxConsecutiveOnes(nums):
    lst = []
    count = 0
    for i in nums:
        if i == 1:
            count += 1
            #print('1')
            #print('count', count)
            lst.append(count)
        else:
            lst.append(count)
            count = 0
            #print('hey'+'2')
            #print('count2', count)
    return max(lst)

print(findMaxConsecutiveOnes([1,0,1,1,0,1]))
'''
#best one
        ret = 0
        cur = 0
        for num in nums:
            if num == 0:
                cur = 0
            else:
                cur += 1
                ret = max(ret,cur)
        return ret
'''